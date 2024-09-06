#!/usr/bin/env python
import agentops
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["AGENTOPS_API_KEY"] = os.getenv('AGENTOPS_API_KEY')

from crewai import Crew
from textwrap import dedent
from config.trip_agents import TripAgents
from config.trip_tasks import TripTasks


class TripCrew:
  def __init__(self, research_question): 
    self.research_question = research_question
    
  def run(self):
    agents = TripAgents()
    tasks = TripTasks()

    lead_farm_researcher = agents.lead_farm_researcher()
    chief_farm_manager = agents.chief_farm_manager()

    conduct_research = tasks.conduct_research(
      lead_farm_researcher, 
      self.research_question
    )

    recommendation_task = tasks.recommendation_task(
      chief_farm_manager,
      self.research_question
    )

    crew = Crew(
      agents=[
        lead_farm_researcher,
        chief_farm_manager
      ],
      tasks=[conduct_research, recommendation_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  agentops.init(os.getenv('AGENTOPS_API_KEY'))
  print("## Welcome to your Farm Management Crew!")
  print('-------------------------------')
  research_question = input(
    dedent("""
      What is your farm question today?
    """))
  trip_crew = TripCrew(research_question)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here is your recommendation!")
  print("########################\n")
  print(result)