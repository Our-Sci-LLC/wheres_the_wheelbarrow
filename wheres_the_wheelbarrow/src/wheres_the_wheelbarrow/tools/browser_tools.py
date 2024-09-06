import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

from langchain_huggingface import HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    endpoint_url=os.getenv('HUGGING_FACE_META_LLAMA_ENDPOINT'),
    huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'),
)
os.environ["BROWSERLESS_API_KEY"] = os.getenv('BROWSERLESS_API_KEY')

# This is taken from https://github.com/crewAIInc/crewAI-examples/blob/main/trip_planner/tools/browser_tools.py
class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          llm=llm,
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)