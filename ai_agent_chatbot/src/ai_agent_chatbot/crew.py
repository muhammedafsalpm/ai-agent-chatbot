from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class AiAgentChatbot():
    """AiAgentChatbot crew with continuous chat"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def chatbot(self) -> Agent:
        return Agent(
            config=self.agents_config['chatbot'],  # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            llm=None  # This will use the default LLM with better capabilities
        )

    @task
    def chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_task'],  # type: ignore[index]
            agent=self.chatbot()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiAgentChatbot crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )