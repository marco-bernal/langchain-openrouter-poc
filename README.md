## Langchain and OpenRourter Integration PoC.

* Langchain/Langgraph used for creating agents and workflows.
* OpenRouter to use LLMs as you go.
* Ollama to use local models.

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

* Run the project: `uv run main.py`

### Next steps:
* Make OpenRouter and Ollama print the streams as they are generated.