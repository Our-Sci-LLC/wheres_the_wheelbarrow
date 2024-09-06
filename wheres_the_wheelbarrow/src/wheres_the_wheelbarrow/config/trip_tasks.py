from crewai import Task
from textwrap import dedent
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class ResearchStrategy(BaseModel):
    """Research report model"""
    geographical_factors: str = Field(..., description="Region or climate factors that would impact practice")
    seasonal_considerations: str = Field(..., description="Seasonal considerations that would impact practice")
    relevant_information: str = Field(..., description="Any other important factors that might influence the practice")
    reliable_sources: List[str] = Field(..., description="A list of reliable resources to find out more information related to practice")
    practical_tips: List[str] = Field(..., description="A list of practical tips related to the practice.")
    variations: List[str] = Field(..., description="A list of different variations that may apply depending on different conditions, such as soil type or weather patterns.")

class TripTasks:

    def conduct_research(self, agent, research_question):
        return Task(
            description=dedent(f"""
                Conduct a comprehensive research on the following farming/agricultural
                question: {research_question}. Your task is to provide a detailed report 
                that includes relevant contextual information to answer the question. 

                Consider geographical factors (such as the region or climate where this practice 
                would be most applicable), seasonal considerations (like the best time of year for
                planting or harvesting), and any other important factors that might influence the answer.

                Make sure you include data from reliable sources, practical tips, and any variations 
                that may apply depending on different conditions (e.g., soil type, weather patterns).

                Make sure you find reliable and relevant information given the current
                year is 2024.

                Research Question: {research_question}

            """),
            agent=agent,
            expected_output="A detailed report covering the direct answer to the research question, geographical context, seasonal context, and any other relevant information",
            output_json=ResearchStrategy
        )

    def recommendation_task(self, agent, research_question): 
        return Task(
            description=dedent(f"""
                Develop a set of
                actionable recommendations tailored to a farmer's specific needs related
                to the research question: {research_question}. The recommendations should be practical, clear, 
                and directly applicable to their farming practices. 

                Consider the geographical context, seasonal factors, soil types, and any
                other relevant information outlined in the research report. Provide step-by-step
                instructions or guidelines where applicable, and suggest any tools, techniques or
                methods that could help the farmer achieve the best outcomes. Additionally 
                include potential challenges and how to address them. 

                Review any provided materials and gather additional information as needed.

                Your final answer should be a comprehensive set of recommendations formmatted 
                clearly, focusing on practical advice and insights that a farmer can immediately 
                use to improve or optimize their farming practice.

                Research Question: {research_question}
            """),
            agent=agent,
            expected_output="A comprehensive set of actionable recommendations for the farmer, including step-by-step instructions, tools, techniques, potential challenges, and ways to address them."
        )