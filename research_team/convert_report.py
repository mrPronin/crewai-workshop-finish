#!/usr/bin/env python3
"""
Local script to convert the existing report.md to HTML
"""

import os
import sys

# Add the scripts directory to the path
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.insert(0, scripts_dir)

if __name__ == '__main__':
    try:
        from convert_to_html import main
        main()
        print("✅ Report converted successfully!")
        print("📁 Check the 'docs' folder for the generated HTML file")
    except ImportError as e:
        print(f"❌ Error importing conversion script: {e}")
        print("Make sure you have installed the required dependencies:")
        print("pip install markdown jinja2 pygments")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
