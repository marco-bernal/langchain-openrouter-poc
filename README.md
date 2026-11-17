## Langchain and OpenRourter PoC. Plus HuggingFace

Contents will be added here. Once the PoC is finished.

### Compatibility notes (Nov 2026):
* Lanchain currently works on python 3.14.6. No support for 3.15 yet.
* Pydantic V1 doesn't support python 3.14. Downgrade to 3.13.

### Install / Setup other python versions
`uv python install 3.13`

`uv python pin 3.13`

`uv sync`

### Run the project

* Set up the `OPENROUTER_API_KEY` env variable:
export `OPENROUTER_API_KEY= my_key`.

* Run the `main.py` file: `python main.py` 

## TODO:
* Implement the huggingface client: https://www.youtube.com/watch?v=1h6lfzJ0wZw
