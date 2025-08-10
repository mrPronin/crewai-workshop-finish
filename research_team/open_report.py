#!/usr/bin/env python3
"""
Open the generated HTML report in the default browser
"""

import os
import webbrowser
from pathlib import Path

def main():
    """Open the HTML report in the default browser"""
    # Get the path to the docs directory
    current_dir = Path(__file__).parent
    docs_dir = current_dir / 'docs'
    html_file = docs_dir / 'index.html'
    
    if html_file.exists():
        # Convert to absolute path and file URL
        abs_path = html_file.absolute()
        file_url = f"file://{abs_path}"
        
        print(f"🌐 Opening report in browser: {file_url}")
        webbrowser.open(file_url)
    else:
        print("❌ HTML file not found. Run 'python convert_report.py' first.")
        print(f"Expected file: {html_file}")

if __name__ == '__main__':
    main()
