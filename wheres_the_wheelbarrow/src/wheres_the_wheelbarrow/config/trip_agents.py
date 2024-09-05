from crewai import Agent
import os
from langchain_huggingface import HuggingFaceEndpoint
endpoint_url = os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT')
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceEndpoint(
    endpoint_url=endpoint_url,
    task="text-generation",
    headers={"Authorization": f"Bearer {api_token}"}
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