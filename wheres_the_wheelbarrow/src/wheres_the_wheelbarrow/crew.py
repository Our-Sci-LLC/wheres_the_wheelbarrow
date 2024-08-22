from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

from wheres_the_wheelbarrow.tools.custom_tool import DatabaseInitializer, DatabaseInsert, DatabaseRetrieval

from langchain_cohere import ChatCohere
from dotenv import load_dotenv

# Initialize language model
load_dotenv()
os.environ["COHERE_API_KEY"] = os.getenv('COHERE_API_KEY')
llm = ChatCohere()

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# loading tools
database_start_tool = DatabaseInitializer()
database_insert_tool = DatabaseInsert()
database_retrieval_tool = DatabaseRetrieval()
#image_processing_tool = ImageRetrievalTool()

@CrewBase
class WheresTheWheelbarrowCrew():
	"""WheresTheWheelbarrow crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def image_recognition(self) -> Agent:
		return Agent(
			config=self.agents_config['image_recognition'],
			verbose=True,
			llm=llm
		)

	@agent
	def image_processor(self) -> Agent:
		return Agent(
			config=self.agents_config['image_processor'],
			verbose=True,
			human_input=True,
			#tools=[image_processing_tool],
			llm=llm
		) 
	"""

	@agent
	def inventory_management(self) -> Agent:
		return Agent(
			config=self.agents_config['inventory_management'],
			verbose=True,
			llm=llm
		)

	@agent
	def database_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['database_developer'],
			verbose=True,
			tools=[database_start_tool, database_insert_tool, database_retrieval_tool],
			llm=llm
		)

	""" 
	@task
	def image_processing_task(self) -> Task:
		return Task(
			config=self.tasks_config['image_processing_task'],
			human_input=True
		) 
		

	@task
	def image_recognition_task(self) -> Task:
		return Task(
			config=self.tasks_config['image_recognition_task'],
		) 
		
	"""


	@task
	def inventory_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_management_task'],
		)

	@task
	def database_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['database_management_task'],
		)

	@task
	def inventory_insert_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_insert_task'],
		)

	@task
	def inventory_retrieval_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_retrieval_task'],
			human_input=True
		) """

	@crew
	def crew(self) -> Crew:
		"""Creates the WheresTheWheelbarrow crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			planning=True,
			planning_llm=llm
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)