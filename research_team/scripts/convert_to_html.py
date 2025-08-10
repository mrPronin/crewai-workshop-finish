#!/usr/bin/env python3
"""
Convert markdown report to HTML for GitHub Pages
"""

import os
import sys
import markdown
from datetime import datetime
from jinja2 import Template

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def read_markdown_file(file_path):
    """Read the markdown file and return its content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def convert_markdown_to_html(markdown_content):
    """Convert markdown content to HTML"""
    # Configure markdown extensions for better rendering
    extensions = [
        'markdown.extensions.toc',
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists'
    ]
    
    extension_configs = {
        'codehilite': {
            'css_class': 'highlight',
            'use_pygments': True,
            'noclasses': True
        }
    }
    
    md = markdown.Markdown(
        extensions=extensions,
        extension_configs=extension_configs
    )
    
    return md.convert(markdown_content)

def get_html_template():
    """Return the HTML template for the report"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #64748b;
            --background-color: #ffffff;
            --text-color: #1e293b;
            --border-color: #e2e8f0;
            --code-bg: #f1f5f9;
            --highlight-bg: #fef3c7;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 2px solid var(--border-color);
        }

        .header h1 {
            font-size: 2.5rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .header .meta {
            color: var(--secondary-color);
            font-size: 1.1rem;
        }

        .content {
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .content h1, .content h2, .content h3, .content h4, .content h5, .content h6 {
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
            font-weight: 600;
        }

        .content h1 {
            font-size: 2rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.5rem;
        }

        .content h2 {
            font-size: 1.75rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.25rem;
        }

        .content h3 {
            font-size: 1.5rem;
        }

        .content h4 {
            font-size: 1.25rem;
        }

        .content p {
            margin-bottom: 1rem;
        }

        .content ul, .content ol {
            margin-bottom: 1rem;
            padding-left: 2rem;
        }

        .content li {
            margin-bottom: 0.5rem;
        }

        .content blockquote {
            border-left: 4px solid var(--primary-color);
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
            color: var(--secondary-color);
        }

        .content code {
            background-color: var(--code-bg);
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.9em;
        }

        .content pre {
            background-color: var(--code-bg);
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin: 1rem 0;
        }

        .content pre code {
            background: none;
            padding: 0;
        }

        .content table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }

        .content th, .content td {
            border: 1px solid var(--border-color);
            padding: 0.75rem;
            text-align: left;
        }

        .content th {
            background-color: var(--code-bg);
            font-weight: 600;
        }

        .content img {
            max-width: 100%;
            height: auto;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }

        .footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 2px solid var(--border-color);
            text-align: center;
            color: var(--secondary-color);
        }

        .toc {
            background-color: var(--code-bg);
            padding: 1.5rem;
            border-radius: 0.5rem;
            margin: 2rem 0;
        }

        .toc h2 {
            margin-top: 0;
            color: var(--primary-color);
        }

        .toc ul {
            list-style: none;
            padding-left: 0;
        }

        .toc li {
            margin-bottom: 0.5rem;
        }

        .toc a {
            color: var(--text-color);
            text-decoration: none;
            transition: color 0.2s;
        }

        .toc a:hover {
            color: var(--primary-color);
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }

            .header h1 {
                font-size: 2rem;
            }

            .content {
                font-size: 1rem;
            }
        }

        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            :root {
                --background-color: #0f172a;
                --text-color: #f1f5f9;
                --border-color: #334155;
                --code-bg: #1e293b;
                --highlight-bg: #451a03;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{ title }}</h1>
            <div class="meta">
                Generated on {{ generation_date }}
            </div>
        </div>

        <div class="content">
            {{ content }}
        </div>

        <div class="footer">
            <p>Generated by ResearchTeam Crew using crewAI</p>
            <p>Last updated: {{ generation_date }}</p>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
</body>
</html>
"""

def create_docs_directory():
    """Create the docs directory if it doesn't exist"""
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    return docs_dir

def main():
    """Main function to convert markdown to HTML"""
    # Get the path to the markdown file
    project_root = os.path.dirname(os.path.dirname(__file__))
    markdown_file = os.path.join(project_root, 'report.md')
    
    # Read the markdown content
    markdown_content = read_markdown_file(markdown_file)
    if markdown_content is None:
        sys.exit(1)
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(markdown_content)
    
    # Get the title from the first line
    lines = markdown_content.strip().split('\n')
    title = lines[0].replace('# ', '') if lines and lines[0].startswith('# ') else 'Research Report'
    
    # Create the docs directory
    docs_dir = create_docs_directory()
    
    # Render the HTML template
    template = Template(get_html_template())
    html_output = template.render(
        title=title,
        content=html_content,
        generation_date=datetime.now().strftime('%B %d, %Y at %I:%M %p')
    )
    
    # Write the HTML file
    output_file = os.path.join(docs_dir, 'index.html')
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Successfully converted markdown to HTML: {output_file}")
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
