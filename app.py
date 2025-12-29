from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
import markdown
from datetime import datetime
from rapidfuzz import fuzz, process
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Markdown with extensions
md = markdown.Markdown(extensions=[
    'fenced_code',
    'tables',
    'toc',
    'extra'
])


def load_blog_posts():
    """Load all blog posts from markdown files"""
    posts = []
    posts_dir = app.config['POSTS_DIR']

    if not os.path.exists(posts_dir):
        return posts

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

                # Parse frontmatter (simple YAML-like format)
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1].strip()
                        post_content = parts[2].strip()

                        # Parse frontmatter
                        metadata = {}
                        for line in frontmatter.split('\n'):
                            if ':' in line:
                                key, value = line.split(':', 1)
                                key = key.strip()
                                value = value.strip()

                                if key == 'keywords':
                                    metadata[key] = [k.strip() for k in value.split(',')]
                                elif key == 'date':
                                    metadata[key] = value
                                else:
                                    metadata[key] = value

                        post = {
                            'id': filename.replace('.md', ''),
                            'slug': filename.replace('.md', ''),
                            'title': metadata.get('title', 'Untitled'),
                            'description': metadata.get('description', ''),
                            'keywords': metadata.get('keywords', []),
                            'date': metadata.get('date', ''),
                            'content': post_content
                        }
                        posts.append(post)

    # Sort by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts


def load_projects():
    """Load all projects from JSON files"""
    projects = []
    projects_dir = app.config['PROJECTS_DIR']

    if not os.path.exists(projects_dir):
        return projects

    for filename in os.listdir(projects_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(projects_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                project = json.load(f)
                projects.append(project)

    return projects


def search_posts(query, posts):
    """Search posts using fuzzy matching"""
    if not query:
        return posts

    results = []
    query_lower = query.lower()

    for post in posts:
        # Calculate fuzzy match scores
        title_score = fuzz.partial_ratio(query_lower, post['title'].lower())
        desc_score = fuzz.partial_ratio(query_lower, post['description'].lower())

        # Check keywords
        keyword_score = 0
        for keyword in post['keywords']:
            score = fuzz.ratio(query_lower, keyword.lower())
            if score > keyword_score:
                keyword_score = score

        # Calculate overall score
        max_score = max(title_score, desc_score, keyword_score)

        if max_score > 60:  # Threshold for fuzzy matching
            results.append({
                'post': post,
                'score': max_score
            })

    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)
    return [r['post'] for r in results]


@app.route('/')
def home():
    """Render home page"""
    return render_template(
        'index.html',
        profile=app.config['PROFILE'],
        tech_stack_line_1=app.config['TECH_STACK_LINE_1'],
        tech_stack_line_2=app.config['TECH_STACK_LINE_2'],
        experience=app.config['EXPERIENCE'],
        education=app.config['EDUCATION'],
        languages=app.config['LANGUAGES'],
        resume_path=app.config['RESUME_PATH']
    )


@app.route('/blog')
def blog():
    """Render blog listing page with pagination"""
    page = request.args.get('page', 1, type=int)
    per_page = 10

    all_posts = load_blog_posts()
    total_posts = len(all_posts)
    total_pages = (total_posts + per_page - 1) // per_page  # Ceiling division

    # Ensure page is within valid range
    page = max(1, min(page, total_pages)) if total_pages > 0 else 1

    # Slice posts for current page
    start = (page - 1) * per_page
    end = start + per_page
    posts = all_posts[start:end]

    return render_template(
        'blog.html',
        posts=posts,
        page=page,
        total_pages=total_pages,
        total_posts=total_posts
    )


@app.route('/blog/<slug>')
def blog_post(slug):
    """Render individual blog post"""
    posts = load_blog_posts()
    post = next((p for p in posts if p['slug'] == slug), None)

    if not post:
        return "Post not found", 404

    # Convert markdown to HTML
    md.reset()
    html_content = md.convert(post['content'])
    post['html_content'] = html_content

    return render_template('post.html', post=post)


@app.route('/projects')
def projects():
    """Render projects page"""
    project_list = load_projects()
    return render_template('projects.html', projects=project_list)


@app.route('/api/search')
def api_search():
    """API endpoint for blog post search"""
    query = request.args.get('q', '')
    posts = load_blog_posts()
    results = search_posts(query, posts)

    # Return simplified data for API
    simplified_results = [
        {
            'title': p['title'],
            'description': p['description'],
            'slug': p['slug'],
            'keywords': p['keywords']
        }
        for p in results
    ]

    return jsonify(simplified_results)


@app.route('/resume')
def resume():
    """Serve resume PDF"""
    return send_from_directory('static', 'resume.pdf')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
