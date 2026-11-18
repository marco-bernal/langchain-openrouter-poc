from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# No need to download the model from HF. If exists locally. This avoids wrapping the transformers pipeline.
# Instead, use the HF pipeline directly. See commented code.
transformers_pipeline = pipeline(
    task="text-generation",
    model="mistralai/Ministral-3-3B-Instruct-2512-GGUF",
    max_length=256,
    truncation=True,
)

# e.g:
# from langchain_huggingface import HuggingFacePipeline
#
# llm = HuggingFacePipeline.from_model_id(
#     model_id="./models/my-local-model",   # local path, no download
#     task="text-generation",
#     pipeline_kwargs={"max_new_tokens": 256},
# )
#
# print(llm.invoke("Hello!"))


hf_pipeline = HuggingFacePipeline(pipeline=transformers_pipeline)

template = PromptTemplate.from_template("You are a Senior Backend Java Developer. Please explain in detail the following: {topic}")

chain = template | hf_pipeline
topic = "How to create and use Virtual Threads in Java." # User prompt as parameter

def print_hf_chat():
    hf_response = chain.invoke({"topic": topic})
    print(hf_response)