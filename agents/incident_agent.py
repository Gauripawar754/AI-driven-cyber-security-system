from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)

incident_agent = Agent(
    role = "Incident Response Engineer",
    goal = "Recommend mitigation and response stragies",
    backstory = "SOC response expert skilled in incident containment and recovery",
    verbose = True,
    llm = llm,
    allow_delegation = False
)
