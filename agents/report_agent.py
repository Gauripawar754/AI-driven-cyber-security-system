from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",   
    temperature=0
)

report_agent = Agent(
    role = "Security Reporting Officer",
    goal = "Generate structured cybersecurity incident report",
    backstory = "Compliance expert generating SOC and audit reports",
    verbose = True,
    llm = llm,
    allow_delegation = False
)
