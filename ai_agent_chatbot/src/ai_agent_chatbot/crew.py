from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class ChatbotCrew():
    """Conversational Chatbot Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def chat_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chat_agent'],  # type: ignore[index]
            verbose=False,
            memory=True,  # enables context memory
        )

    @task
    def chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_task'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Chatbot crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )
