"""
Freeze the Flask app into static HTML files for GitHub Pages deployment.

Usage:
    python freeze.py

This will generate static files in the 'build' directory.
"""
import shutil
import os
from flask_frozen import Freezer
from app import app, load_blog_posts, load_projects
from config import Config

# Configure the freezer
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
# Use directories with index.html instead of .html files (e.g., /blog/index.html instead of /blog.html)
app.config['FREEZER_DESTINATION_IGNORE'] = []
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

freezer = Freezer(app)


@freezer.register_generator
def blog_post():
    """Generate URLs for all blog posts."""
    posts = load_blog_posts()
    for post in posts:
        yield {'slug': post['slug']}


@freezer.register_generator
def blog():
    """Generate URLs for paginated blog pages."""
    posts = load_blog_posts()
    per_page = 10
    total_pages = (len(posts) + per_page - 1) // per_page

    # Generate page 1 (default)
    yield {}

    # Generate additional pages
    for page in range(2, total_pages + 1):
        yield {'page': page}


if __name__ == '__main__':
    # Clean docs directory before freezing
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)

    print("Freezing Flask app...")
    freezer.freeze()

    # Create .nojekyll file to prevent GitHub Pages from processing with Jekyll
    nojekyll_path = os.path.join(docs_dir, '.nojekyll')
    open(nojekyll_path, 'w').close()

    # Create CNAME file for custom domain (if configured)
    if Config.DOMAIN:
        cname_path = os.path.join(docs_dir, 'CNAME')
        with open(cname_path, 'w') as f:
            f.write(Config.DOMAIN)

    print("Done! Static files generated in 'docs' directory.")
