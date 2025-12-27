# Personal Portfolio & Blog

A modern, responsive personal portfolio website with integrated blog functionality built with Flask and Tailwind CSS.

## Features

### Home Page
- Professional profile section with photo
- Social media links (LinkedIn, GitHub, Gmail)
- Rotating tech stack display with animations
- Work experience highlights
- Downloadable resume

### Blog
- Markdown-based blog posts with syntax highlighting
- Fuzzy search functionality
- Keyword/tag filtering
- Clean, readable post layout

### Projects
- Project showcase with cover images
- Direct GitHub repository links
- Technology stack display
- Responsive card layout

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Markdown**: python-markdown with Pygments for syntax highlighting
- **Search**: rapidfuzz for fuzzy matching
- **Icons**: Font Awesome

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd blog
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your personal information in `config.py`:
   - Update PROFILE with your name, bio, email, LinkedIn, and GitHub
   - Customize TECH_STACK with your technologies
   - Update WORK_EXPERIENCE with your highlights

5. Add your content:
   - Add blog posts as Markdown files in `content/posts/`
   - Add project JSON files in `content/projects/`
   - Add your profile image to `static/images/profile.jpg`
   - Add your resume PDF to `static/resume.pdf`

## Running the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Blog Post Format

Create Markdown files in `content/posts/` with the following frontmatter:

```markdown
---
title: Your Post Title
description: A brief description of your post
keywords: python, flask, web development
date: 2025-01-15
---

# Your Content Here

Write your blog post content using Markdown...
```

## Project Format

Create JSON files in `content/projects/` with the following structure:

```json
{
  "id": "project-slug",
  "title": "Project Title",
  "description": "Project description",
  "cover_image": "/static/images/projects/cover.jpg",
  "github_url": "https://github.com/username/repo",
  "technologies": ["Python", "Flask", "Docker"]
}
```

## File Structure

```
/blog
├── app.py                  # Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── /templates              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── blog.html
│   ├── post.html
│   └── projects.html
├── /static                 # Static assets
│   ├── /css
│   ├── /js
│   ├── /images
│   └── resume.pdf
└── /content                # Content files
    ├── /posts              # Blog posts (Markdown)
    └── /projects           # Project data (JSON)
```

## Customization

### Colors
The default color scheme uses purple and blue gradients. To change colors, update the Tailwind CSS classes in the templates:
- `purple-600`, `purple-700` for primary colors
- `blue-600`, `blue-700` for secondary colors

### Layout
- Modify `templates/base.html` to change the overall layout
- Update individual page templates for specific sections

### Features
The application includes:
- Mobile-responsive navigation
- Syntax highlighting for code blocks
- Real-time search with fuzzy matching
- Animated tech stack rotation
- Hover effects on cards

## Deployment

For production deployment:

1. Set environment variables:
```bash
export SECRET_KEY="your-secret-key"
export FLASK_ENV=production
```

2. Use a production server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. Consider using a reverse proxy (Nginx) and HTTPS

## License

MIT License - feel free to use this template for your own portfolio!

## Credits

Built with:
- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/)
- [Highlight.js](https://highlightjs.org/)
