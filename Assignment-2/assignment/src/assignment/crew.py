from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Import necessary tool for web search
from crewai_tools import SerperDevTool
import os

# Set environment variable for API key
os.environ['SERPER_API_KEY'] = 'e727215d2eeb6917c92b6a15d78718997e306d7f'

@CrewBase
class AssignmentCrew():
    """Crew for building a chatbot that provides information on government services for senior citizens"""

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['search_agent'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['analysis_agent'],
            verbose=True
        )

    @task
    def information_gathering_task(self) -> Task:
        return Task(
            config=self.tasks_config['information_gathering_task'],
        )

    @task
    def information_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['information_analysis_task'],
            output_file='government_services_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Government Services Chatbot crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
