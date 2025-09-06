.PHONY: clean build

build: fargo.css
	uv run main.py

fargo.css:
	sass ./scss/main.scss ./site/assets/fargo.css

clean:
	rm ./site/assets/fargo.css
