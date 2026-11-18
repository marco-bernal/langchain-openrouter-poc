## Langchain, OpenRourter and HuggingFace Integrations PoC.

* Langchain/Langgraph used for creating agents and workflows.
* OpenRouter to use LLMs as you go.
* HuggingFace for using experimental LLMs locally.

With the tools above it is possible to create multimodel agentic workflows.

Polish this description. Once the PoC is finished.

### Compatibility notes (Nov 2026):
* `Lanchain-OpenRouter` currently works on python 3.14.6. No support for 3.15 yet.
* `Pydantic V1` doesn't support python 3.14. Downgrade to 3.13.

### Install / Setup other python versions
`uv python install 3.13`

`uv python pin 3.13`

`uv sync`

### Run the project

* Set up the `OPENROUTER_API_KEY` env variable. Either, in the run config of PyCharm or as env variable on the console: 
export `OPENROUTER_API_KEY= my_key`.

* Run the `main.py` file: `python main.py` 

## TODO:
* Add timers and compare how long it takes for every client to respond.

### Next steps:
* Create my first agent (Langchain/Langgraph and OpenRouter): Tech with Tim.
* Update and Run code from TL:DR to use it in my machine. (Langchain/Langgraph and OpenRouter)
