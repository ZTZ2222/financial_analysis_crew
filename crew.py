from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI


@CrewBase
class TradingCrew:
    """Trading crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    """Agents"""

    @agent
    def data_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["data_analyst_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    @agent
    def tading_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tading_strategy_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    @agent
    def execution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["execution_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    @agent
    def risk_management_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_management_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    """Tasks"""

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["data_analysis_task"],
            agent=self.data_analyst_agent(),
        )

    @task
    def strategy_development_task(self) -> Task:
        return Task(
            config=self.tasks_config["strategy_development_task"],
            agent=self.tading_strategy_agent(),
        )

    @task
    def execution_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["execution_planning_task"],
            agent=self.execution_agent(),
        )

    @task
    def risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["risk_assessment_task"],
            agent=self.risk_management_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Linkedin crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
            verbose=True,
        )
