from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",  
    temperature=0
)


threat_agent = Agent(
    role = "Cyber Threat Analyst",
    goal = "Detect suspecious activities and cyber attacks from logs",
    backstory = "Expert SOC analyst skilled in threat detection and MITRE ATT&CK",
    verbose = True,
    llm = llm,
    allow_delegations = False
)
