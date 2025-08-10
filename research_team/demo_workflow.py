#!/usr/bin/env python3
"""
Demo workflow: Generate report, convert to HTML, and open in browser
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error during {description}: {e}")
        return False

def main():
    """Run the complete workflow"""
    print("🚀 ResearchTeam Crew - Complete Workflow Demo")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("report.md").exists():
        print("⚠️  No existing report.md found. This demo will show the conversion process.")
        print("   To generate a new report, run: crewai run")
    
    # Step 1: Convert markdown to HTML
    if not run_command("python convert_report.py", "Converting markdown to HTML"):
        print("\n💡 Make sure you have the required dependencies installed:")
        print("   pip install markdown jinja2 pygments")
        return
    
    # Step 2: Check if HTML was created
    html_file = Path("docs/index.html")
    if not html_file.exists():
        print("❌ HTML file was not created")
        return
    
    print(f"📄 HTML file created: {html_file}")
    print(f"📊 File size: {html_file.stat().st_size / 1024:.1f} KB")
    
    # Step 3: Open in browser
    print("\n🌐 Opening report in browser...")
    try:
        import webbrowser
        abs_path = html_file.absolute()
        file_url = f"file://{abs_path}"
        webbrowser.open(file_url)
        print("✅ Report opened in browser")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print(f"💡 You can manually open: {file_url}")
    
    # Step 4: Show next steps
    print("\n🎉 Workflow completed!")
    print("\n📋 Next steps:")
    print("1. Review the report in your browser")
    print("2. To deploy to GitHub Pages:")
    print("   - Push your changes to GitHub")
    print("   - Enable GitHub Pages in repository settings")
    print("   - The report will automatically deploy")
    print("\n📚 For more information, see: GITHUB_PAGES.md")

if __name__ == '__main__':
    main()
