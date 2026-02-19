import os

from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

from agents.threat_agent import threat_agent
from agents.vulnerability_agent import vulnerability_agent
from agents.report_agent import report_agent
from agents.incident_agent import incident_agent

from crewai import Crew

from tasks.incident_task import incident_task
from tasks.report_task import report_task
from tasks.threat_task import threat_task
from tasks.vulnerabiltiy_task import vulnerabilty_task

from tools.cve_rag import build_cve_vectorstore, retrieve_relevant_cves

vectorstore = build_cve_vectorstore("data/nvdcve.json")


threat_summary = "PowerShell execution and privilege escalation detected"

relevant_cves = retrieve_relevant_cves(vectorstore, threat_summary)




logs = open("data/adsystem_logs.txt").read()
cve = open("data/nvdcve.json", encoding="utf-8").read()


# tasks

task1 = threat_task(threat_agent, logs)
task2 = vulnerabilty_task(
    threat_summary,
    vulnerability_agent,
    relevant_cves
)
task3 = incident_task(incident_agent, "{output of task2}")
task4 = report_task(report_agent, "{output of task3}")



crew = Crew(
    agents=[threat_agent, vulnerability_agent, incident_agent, report_agent],
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process="sequential"
)

result = crew.kickoff()

print(result)
