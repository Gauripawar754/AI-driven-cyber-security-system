import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

print("API KEY:", os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("Say hello in one sentence.")
print(response.content)