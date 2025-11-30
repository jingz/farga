.PHONY: clean build open help

help:
	@echo "Help: Commands that you can use."
	@echo "==============================="
	@echo "build    Compile all sass files and HTML templates into docs and css."
	@echo "open     Open the built document website."

build: farga.css farga.all.css
	uv run main.py

open:
	open site/index.html

farga.css:
	sass --style=compressed ./scss/main.scss ./site/assets/farga.css

farga.all.css:
	sass ./scss/all.scss ./site/assets/farga.all.css

clean:
	rm ./site/assets/farga.css
