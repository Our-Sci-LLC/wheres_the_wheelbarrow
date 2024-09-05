from crewai import Task
from textwrap import dedent
from datetime import date

class TripTasks:

    def identify_task(self, agent):
        return Task(
            description=dedent(f"""
                Write a charming short story about a farmer and their
                farm hand. This task involves writing a complete story. 
                
                Your final answer must be a story no longer than 350 words.
                {self.__tip_section()}

            """),
            agent=agent,
            expected_output="Short story about a farm"
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"