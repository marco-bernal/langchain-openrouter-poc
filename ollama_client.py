from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

ollama_model = ChatOllama(model="qwen3.5:4b")

template = PromptTemplate.from_template("You are a Senior Backend Java Developer. Please explain in detail the following: {topic}")

chain = template | ollama_model
topic = "How to create and use Virtual Threads in Java." # User prompt as parameter

def print_ollama_chat():
    response = chain.invoke({"topic": topic})
    print(response)