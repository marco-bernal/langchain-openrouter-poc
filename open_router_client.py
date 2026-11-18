from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate

open_router_model = ChatOpenRouter(
    model="anthropic/claude-sonnet-4.6",
    temperature=0.8,
)

template = PromptTemplate.from_template("You are a Senior Backend Java Developer. Please explain in detail the following: {topic}")

chain = template | open_router_model
topic = "How the create and use Virtual Threads in Java 25. If that version is too new, downgrade to Java 24." # User prompt as parameter

def print_open_router_chat():
    response = chain.invoke({"topic": topic})
    print(response)