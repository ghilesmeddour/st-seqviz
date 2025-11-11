.PHONY: demo

demo:
	uv sync --extra demo
	uv run streamlit run ./demo/main.py

front:
	npm --prefix st_seqviz/frontend install
	npm --prefix st_seqviz/frontend run build

build:
	make front
	uv build
