from crewai import Agent, Crew, Process, Task
from crewai.project import (
        CrewBase,
        agent,
        crew,
        task,
        before_kickoff,
        after_kickoff
    )
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool
import os
import sys

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class ResearchTeam():
    """ResearchTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents:
    # https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks:
    # https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents,
    # you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],  # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchTeam crew"""
        # To learn how to add knowledge sources to your crew,
        # check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            # Automatically created by the @agent decorator
            agents=self.agents,
            # Automatically created by the @task decorator
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical,
            # In case you wanna use that instead
            # https://docs.crewai.com/concepts/crews#hierarchical/
        )

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs  # You can return the inputs or modify them as needed

    @after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        
        # Convert markdown to HTML after the report is generated
        try:
            self._convert_to_html()
        except Exception as e:
            print(f"Warning: Failed to convert to HTML: {e}")
        
        return result  # You can return the result or modify it as needed

    def _convert_to_html(self):
        """Convert the generated markdown report to HTML"""
        try:
            # Get the path to the convert script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            convert_script = os.path.join(project_root, 'scripts', 'convert_to_html.py')
            
            if os.path.exists(convert_script):
                # Run the conversion script
                import subprocess
                result = subprocess.run(
                    [sys.executable, convert_script],
                    cwd=project_root,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    print("✅ Successfully converted report to HTML for GitHub Pages")
                else:
                    print(f"❌ Failed to convert to HTML: {result.stderr}")
            else:
                print("⚠️  HTML conversion script not found")
                
        except Exception as e:
            print(f"❌ Error during HTML conversion: {e}")
