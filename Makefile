.PHONY: clean build

build: farga.css farga.all.css
	uv run main.py

farga.css:
	sass --style=compressed ./scss/main.scss ./site/assets/farga.css

farga.all.css:
	sass ./scss/all.scss ./site/assets/farga.all.css

clean:
	rm ./site/assets/farga.css
