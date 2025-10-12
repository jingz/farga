.PHONY: clean build

build: farga.css
	uv run main.py

farga.css:
	sass ./scss/main.scss ./site/assets/farga.css

clean:
	rm ./site/assets/farga.css
