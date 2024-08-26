from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

#from wheres_the_wheelbarrow.tools.custom_tool import DatabaseInitializer, DatabaseInsert, DatabaseRetrieval

from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

# Initialize language model
load_dotenv()

# To use Cohere model, use these - free model forever(?)
#os.environ["COHERE_API_KEY"] = os.getenv('COHERE_API_KEY')
#llm = ChatCohere()

# To use local llama (is actually on rose's computer) - the base_url needs to be changed and the server up to actually work (works 1/7 times running crewai run)
os.environ["OPENAI_API_KEY"] = "NA"
#ip_address = os.getenv('OLLAMA_HOST')

llm = ChatOllama(
    model = "llama3.1",
    base_url = "https://e4b7-97-132-96-25.ngrok-free.app")

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# loading tools
#database_start_tool = DatabaseInitializer()
#database_insert_tool = DatabaseInsert()
#database_retrieval_tool = DatabaseRetrieval()
#image_processing_tool = ImageRetrievalTool()

@CrewBase
class WheresTheWheelbarrowCrew():
    """WheresTheWheelbarrow crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def image_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['image_processor'],
            verbose=True,
            llm=llm,
            allow_delegation=False
        ) 
    
    @task
    def image_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task'],
            human_input=True
        ) 

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