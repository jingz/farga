.PHONY: clean build check open help

help:
	@echo "Help: Commands that you can use."
	@echo "==============================="
	@echo "build    Compile all sass files and HTML templates into docs and css."
	@echo "check    Build, then run the accessibility and design-system checks."
	@echo "open     Open the built document website."

build: farga.css farga.all.css
	@uv run main.py > /dev/null

check: build
	uv run python check.py

open:
	open site/index.html

farga.css:
	sass --style=compressed ./scss/main.scss ./site/assets/farga.css

farga.all.css:
	sass ./scss/all.scss ./site/assets/farga.all.css

clean:
	rm ./site/assets/farga.css
