# ResearchTeam Crew

Welcome to the ResearchTeam Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## ✨ New Feature: GitHub Pages Integration

This project now includes **automatic GitHub Pages deployment**! When you generate a research report, it's automatically converted to a beautiful HTML website and deployed to GitHub Pages.

### 🚀 Quick Start with GitHub Pages

1. **Enable GitHub Pages** in your repository settings
2. **Install dependencies**: `pip install markdown jinja2 pygments`
3. **Generate a report**: `crewai run`
4. **Push to GitHub**: The report will automatically be deployed to GitHub Pages!

For detailed setup instructions, see [GITHUB_PAGES.md](GITHUB_PAGES.md).

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/research_team/config/agents.yaml` to define your agents
- Modify `src/research_team/config/tasks.yaml` to define your tasks
- Modify `src/research_team/crew.py` to add your own logic, tools and specific args
- Modify `src/research_team/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the research-team Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

### 🌐 View Your Report Online

After running the crew, you can:

1. **Convert to HTML locally**:
   ```bash
   python convert_report.py
   ```

2. **Open in browser**:
   ```bash
   python open_report.py
   ```

3. **Deploy to GitHub Pages** (if using GitHub):
   - Push your changes to the main branch
   - The report will automatically be deployed to GitHub Pages

## Understanding Your Crew

The research-team Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## 📁 Project Structure

```
research_team/
├── .github/workflows/          # GitHub Actions for auto-deployment
├── scripts/                    # HTML conversion utilities
├── docs/                       # Generated static site (auto-created)
├── src/research_team/          # Main crew implementation
├── report.md                   # Generated research report
├── convert_report.py           # Local HTML conversion
├── open_report.py              # Open report in browser
└── GITHUB_PAGES.md            # GitHub Pages setup guide
```

## Support

For support, questions, or feedback regarding the ResearchTeam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
