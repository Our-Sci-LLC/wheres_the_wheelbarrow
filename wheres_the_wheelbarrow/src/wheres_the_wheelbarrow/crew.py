from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from wheres_the_wheelbarrow.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class WheresTheWheelbarrowCrew():
	"""WheresTheWheelbarrow crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def image_recognition(self) -> Agent:
		return Agent(
			config=self.agents_config['image_recognition'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def inventory_management(self) -> Agent:
		return Agent(
			config=self.agents_config['inventory_management'],
			verbose=True
		)

	@task
	def image_recognition_task(self) -> Task:
		return Task(
			config=self.tasks_config['image_recognition_task'],
		)

	@task
	def inventory_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_management_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the WheresTheWheelbarrow crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)