from crewai import Agent
import os
from langchain_huggingface import HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()
#os.environ["OPENAI_API_BASE"]=os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT')
#os.environ["OPENAI_MODEL_NAME"]='llama-2-7b-chat-hf-fie'
#os.environ["OPENAI_API_KEY"]=os.getenv('HUGGINGFACEHUB_API_TOKEN')

#llm = ChatOpenAI(openai_api_base=os.environ.get("HUGGING_FACE_META_LLAMA_ENDPOINT"),
#                 openai_api_key=os.environ.get('HUGGINGFACEHUB_API_TOKEN'),
#                 model_name='llama-2-7b-chat-hf-fie')

llm = HuggingFaceEndpoint(
    endpoint_url=os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT'),
    huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'),
)

class TripAgents():

  def city_selection_agent(self):
    return Agent(
        role='Storytelling expert',
        goal='Tell a charming story about a farmhand.',
        backstory=
        'An expert in weaving together tales',
        verbose=True,
        llm=llm)