#!/usr/bin/env python
import agentops
import os
os.environ["AGENTOPS_API_KEY"] = os.getenv('AGENTOPS_API_KEY')

from crewai import Crew
from textwrap import dedent
from config.trip_agents import TripAgents
from config.trip_tasks import TripTasks

from dotenv import load_dotenv
load_dotenv()

class TripCrew:
  def __init__(self, photo):
    self.photo = photo

  def run(self):
    agentops.init()
    agents = TripAgents()
    tasks = TripTasks()

    city_selection_agent = agents.city_selection_agent()

    identify_task = tasks.identify_task(
      city_selection_agent,
      self.photo
    )

    crew = Crew(
      agents=[
        city_selection_agent
      ],
      tasks=[identify_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Farm Management Crew!")
  print('-------------------------------')
  photo = input(
    dedent("""
      What is the photo URL?
    """))
  
  trip_crew = TripCrew(photo)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here are the objects extracted from the image!")
  print("########################\n")
  print(result)