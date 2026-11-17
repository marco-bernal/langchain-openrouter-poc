from langchain_openrouter import ChatOpenRouter


model = ChatOpenRouter(
    model="anthropic/claude-sonnet-4.6",
    temperature=0.8,
)

def print_chat():
    # Example usage
    response = model.invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?")
    print(response.content)