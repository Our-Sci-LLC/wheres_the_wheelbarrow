#from agentops import track_agent
#from crewai import Agent, Crew, Process, Task
#from crewai.project import CrewBase, agent, crew, task
#import os

#from langchain_cohere import ChatCohere
#from langchain_ollama import ChatOllama
#from openai import OpenAI

#from dotenv import load_dotenv
#from langchain_huggingface import HuggingFaceEndpoint

# Found some tracking tools that might potentially tell us why nothing works?
# This HAS to be the first thing
#import agentops
#os.environ["AGENTOPS_API_KEY"] = os.getenv('AGENTOPS_API_KEY')
#agentops.init()

# Initialize language model
#load_dotenv()

# These are all fragmented pieces used to run different types of models ... 

# To use Cohere model, use these - free model forever(?)
#os.environ["COHERE_API_KEY"] = os.getenv('COHERE_API_KEY')
#llm = ChatCohere()

# To use local llama (is actually on rose's computer) - the base_url needs to be changed and the server up to actually work (works 1/7 times running crewai run)
#os.environ["OPENAI_API_KEY"] = "NA"
#ip_address = os.getenv('OLLAMA_HOST')

#os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
#os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
#os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('OPENAI_API_KEY')
#os.environ["OPENAI_API_BASE"] = '' # this should probably be in secrets 
#os.environ["OPENAI_MODEL_NAME"] = 'Meta-llama-3-1-8b-instruct-vno'
#llm = OpenAI()
#llm = HuggingFaceEndpoint(
#    endpoint_url = '' # redacted for now
#)

# Setup to use inference endpoints 
# Variables are in github secrets 
#endpoint_url = os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT')
#api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

#llm = HuggingFaceEndpoint(
#    endpoint_url=endpoint_url,
#    task="text-generation",
#    headers={"Authorization": f"Bearer {api_token}"}
#)

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# loading tools
#database_start_tool = DatabaseInitializer()
#database_insert_tool = DatabaseInsert()
#database_retrieval_tool = DatabaseRetrieval()
#image_processing_tool = ImageRetrievalTool()

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

	
""" 	@task
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
		) 



    @agent
    def image_recognizer(self) -> Agent:
        return Agent(
            config=self.agents_config['image_recognizer'],
            verbose=True,
            llm=llm
        ) 
    
    @task
    def image_recognizing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_recognizing_task']
        ) 


		    @agent
    def image_recognizer(self) -> Agent:
        return Agent(
            config=self.agents_config['image_recognizer'],
            verbose=True,
            llm=llm
        ) 
    
    @task
    def image_recognizing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task']
        ) 


from agentops import track_agent
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

#from wheres_the_wheelbarrow.tools.custom_tool import DatabaseInitializer, DatabaseInsert, DatabaseRetrieval

from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
from openai import OpenAI

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

# Found some tracking tools that might potentially tell us why nothing works?
# This HAS to be the first thing
import agentops
os.environ["AGENTOPS_API_KEY"] = os.getenv('AGENTOPS_API_KEY')
agentops.init()

# Initialize language model
load_dotenv()

# These are all fragmented pieces used to run different types of models ... 

# To use Cohere model, use these - free model forever(?)
#os.environ["COHERE_API_KEY"] = os.getenv('COHERE_API_KEY')
#llm = ChatCohere()

# To use local llama (is actually on rose's computer) - the base_url needs to be changed and the server up to actually work (works 1/7 times running crewai run)
#os.environ["OPENAI_API_KEY"] = "NA"
#ip_address = os.getenv('OLLAMA_HOST')

#os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
#os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
#os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('OPENAI_API_KEY')
#os.environ["OPENAI_API_BASE"] = '' # this should probably be in secrets 
#os.environ["OPENAI_MODEL_NAME"] = 'Meta-llama-3-1-8b-instruct-vno'
#llm = OpenAI()
#llm = HuggingFaceEndpoint(
#    endpoint_url = '' # redacted for now
#)

# Setup to use inference endpoints 
# Variables are in github secrets 
endpoint_url = os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT')
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceEndpoint(
    endpoint_url=endpoint_url,
    task="text-generation",
    headers={"Authorization": f"Bearer {api_token}"}
)

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

    @track_agent(name="First Agent: Image Processor")
    @agent
    def image_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['image_processor'],
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iterations=100,
            timeout=300 # (5 minutes)
        ) 
    
    @task
    def image_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task'],
            human_input=False
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
		

@CrewBase
class WheresTheWheelbarrowCrew():
    """WheresTheWheelbarrow crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @track_agent(name="First Agent: Image Processor")
    @agent
    def image_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['image_processor'],
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iterations=100,
            timeout=300 # (5 minutes)
        ) 
    
    @task
    def image_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task'],
            human_input=False
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
