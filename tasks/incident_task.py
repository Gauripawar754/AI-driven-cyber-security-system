from crewai import Task

def incident_task(agent, vulnerabilities):
    return Task(
        description = f""" 
        Given the vulnerabilities below:
        {vulnerabilities}

        Suggest the incident reponse and mitigation steps.
        """,
        agent = agent,
        expected_output = "Structured information about incident reponse action mitigation steps"
    )