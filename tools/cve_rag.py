import json
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.docstore.document import Document

def build_cve_vectorstore(cve_file_path):
    with open(cve_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    vulnerabilities = data.get("vulnerabilities", [])

    for item in vulnerabilities[:2000]:  # limit for demo
        cve_data = item.get("cve", {})

        cve_id = cve_data.get("id", "Unknown CVE")

        descriptions = cve_data.get("descriptions", [])
        description_text = ""

        for desc in descriptions:
            if desc.get("lang") == "en":
                description_text = desc.get("value")
                break

        text = f"CVE ID: {cve_id}\nDescription: {description_text}"

        documents.append(Document(page_content=text))

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vectorstore = FAISS.from_documents(documents, embeddings)

    return vectorstore

def retrieve_relevant_cves(vectorstore, query, k=3):
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])