from crewai import Task

def threat_task(agent, logs):
    return Task(
        description = f""" 
        Analyze the following system logs and identify possible cyber threats:
        {logs}
                
        Detect brute force attacks, suspecious IPs, anomalies, unauthorized access attempts, malware infections, data exfiltration and Denial of Service 
        """,
        agent = agent, 
        expected_output = "List of detected cyber threats with their explanations"
    )