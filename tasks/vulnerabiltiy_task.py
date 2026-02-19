from crewai import Task

def vulnerabilty_task(threats,agent, cve_data):
    return Task(
        description = f"""
        Based on these detected threats:
        {threats}
        Map them to their relevant CVEs using this data:
        {cve_data}
        Assign severity using CVSS scores.
        """,
        config={},
        agent = agent,
        expected_output = "Table containing Threat-to-CVE mapping with severity levels and CVSS Scores "
        
    )
