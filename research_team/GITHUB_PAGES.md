# GitHub Pages Integration

This project now includes automatic GitHub Pages deployment! When you generate a new research report, it will automatically be converted to a beautiful HTML website and deployed to GitHub Pages.

## Features

- ✅ **Automatic HTML Conversion**: Markdown reports are automatically converted to responsive HTML
- ✅ **Beautiful Design**: Modern, responsive design with dark mode support
- ✅ **GitHub Actions**: Automated deployment on every report update
- ✅ **Syntax Highlighting**: Code blocks are properly highlighted
- ✅ **Mobile Friendly**: Responsive design that works on all devices

## Setup Instructions

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. Save the changes

### 2. Configure Repository Settings

Make sure your repository has the following settings:

- **Repository visibility**: Public (required for free GitHub Pages)
- **Branch protection**: Main branch should be protected
- **Actions permissions**: Allow GitHub Actions to run

### 3. Install Dependencies

Install the required dependencies for HTML conversion:

```bash
cd research_team
pip install markdown jinja2 pygments
```

Or update your existing installation:

```bash
pip install -e .
```

## How It Works

### Automatic Workflow

1. **Report Generation**: When you run `crewai run`, the system generates a `report.md` file
2. **HTML Conversion**: The system automatically converts the markdown to HTML using a beautiful template
3. **GitHub Actions**: When you push the updated report to the main branch, GitHub Actions automatically:
   - Converts the markdown to HTML
   - Builds the static site
   - Deploys it to GitHub Pages

### Manual Conversion

You can also convert the report manually:

```bash
cd research_team
python convert_report.py
```

This will create a `docs/index.html` file that you can view locally.

## File Structure

```
research_team/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── scripts/
│   ├── __init__.py
│   └── convert_to_html.py      # HTML conversion script
├── docs/                       # Generated static site (created automatically)
│   └── index.html
├── report.md                   # Generated research report
├── convert_report.py           # Local conversion script
└── GITHUB_PAGES.md            # This file
```

## Customization

### Styling

The HTML template includes modern CSS with:
- Responsive design
- Dark mode support
- Syntax highlighting
- Beautiful typography
- Mobile-friendly layout

You can customize the styling by editing the CSS in `scripts/convert_to_html.py`.

### Template

The HTML template is defined in the `get_html_template()` function in `scripts/convert_to_html.py`. You can modify it to:
- Add your own branding
- Include additional meta tags
- Add analytics
- Customize the layout

### GitHub Actions

The workflow file `.github/workflows/deploy.yml` can be customized to:
- Change the trigger conditions
- Add additional build steps
- Modify the deployment process
- Add notifications

## Troubleshooting

### Common Issues

1. **GitHub Pages not updating**
   - Check the Actions tab in your repository
   - Ensure the workflow completed successfully
   - Verify GitHub Pages is enabled in repository settings

2. **HTML conversion fails**
   - Install required dependencies: `pip install markdown jinja2 pygments`
   - Check that `report.md` exists
   - Verify Python version (3.10+)

3. **Styling issues**
   - Clear browser cache
   - Check for CSS conflicts
   - Verify the HTML file was generated correctly

### Debugging

1. **Check GitHub Actions logs**:
   - Go to Actions tab in your repository
   - Click on the latest workflow run
   - Check the build logs for errors

2. **Test locally**:
   ```bash
   cd research_team
   python convert_report.py
   ```
   Then open `docs/index.html` in your browser

3. **Verify file paths**:
   - Ensure `report.md` exists in the project root
   - Check that the `docs` directory is created
   - Verify `index.html` is generated

## Advanced Features

### Custom Domains

You can set up a custom domain for your GitHub Pages site:

1. Go to repository Settings → Pages
2. Under **Custom domain**, enter your domain
3. Add a CNAME file to your repository
4. Configure DNS settings with your domain provider

### Analytics

Add Google Analytics or other tracking:

1. Edit the HTML template in `scripts/convert_to_html.py`
2. Add your analytics code in the `<head>` section
3. Commit and push the changes

### SEO Optimization

The template includes basic SEO features:
- Proper meta tags
- Semantic HTML structure
- Responsive design
- Fast loading times

## Security

- The GitHub Actions workflow uses minimal permissions
- Only the `docs` directory is deployed
- No sensitive data is exposed
- All dependencies are from trusted sources

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review GitHub Actions logs
3. Test the conversion locally
4. Check the crewAI documentation
5. Open an issue in the repository

## Contributing

To improve the GitHub Pages integration:

1. Fork the repository
2. Make your changes
3. Test locally
4. Submit a pull request

## License

This GitHub Pages integration is part of the ResearchTeam project and follows the same license terms.
