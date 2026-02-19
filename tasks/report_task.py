from crewai import Task

def report_task(agent, summery):
    return Task(
        description = f"""
        Generate a proffessional cybersecurity incident report using:
        {summery}

        Include cyber threats, CVEs, CVSS scores, severity and reponse actions.
        """,
        agent = agent,
        expected_output = "SOC-style cybersecurity report"   
    )