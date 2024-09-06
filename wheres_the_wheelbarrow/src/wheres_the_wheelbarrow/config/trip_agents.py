from crewai import Agent
import os
from langchain_huggingface import HuggingFaceEndpoint
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

from dotenv import load_dotenv

load_dotenv()
#os.environ["OPENAI_API_BASE"]=os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT')
#os.environ["OPENAI_MODEL_NAME"]='llama-2-7b-chat-hf-fie'
#os.environ["OPENAI_API_KEY"]=os.getenv('HUGGINGFACEHUB_API_TOKEN')

#llm = ChatOpenAI(openai_api_base=os.environ.get("HUGGING_FACE_META_LLAMA_ENDPOINT"),
#                 openai_api_key=os.environ.get('HUGGINGFACEHUB_API_TOKEN'),
#                 model_name='llama-2-7b-chat-hf-fie')

# This construction is not available anywhere in the documentation but 
# endpoint_url and huggingfacehub_api_token using the HuggingFaceEndpoint 
# is the only way to connect to a HUGGING FACE INFERENCE ENDPOINT (dedicated)
llm = HuggingFaceEndpoint(
    endpoint_url=os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT'),
    huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'),
)

# Everything pretty much based on crewai examples 
# https://github.com/crewAIInc/crewAI-examples/
# Change all these names 
class TripAgents():

  def lead_farm_researcher(self):
    return Agent(
        role='Lead Farm Researcher',
        goal='Conduct amazing analysis of agriculture questions, providing in-depth insights to guide farm strategies.',
        backstory=
        'As the Lead Farm Researcher at a premier research institution, you specialize in dissecting online farm recommendations.',
        tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm=llm)

  def chief_farm_manager(self):
    return Agent(
        role='Chief Farm Manager',
        goal='Synthesize amazing insights from research analysis to formulate incredible farm recommendations.',
        backstory=
        'You are the Chief Farm Manager at a leading agricultural operation, known for crafting bespoke recommendations that drive success.',
        tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_website
        ],
        verbose=True,
        llm=llm)