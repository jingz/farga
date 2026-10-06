.PHONY: clean build check size open help

help:
	@echo "Help: Commands that you can use."
	@echo "==============================="
	@echo "build    Compile all sass files and HTML templates into docs and css."
	@echo "check    Build, then run the accessibility and design-system checks."
	@echo "size     Print shipped artifact sizes, raw and compressed."
	@echo "open     Open the built document website."

build: farga.css farga.all.css
	@uv run main.py > /dev/null

check: build
	uv run python check.py

size: farga.css farga.all.css
	@printf '%-16s %10s %10s %12s\n' artifact raw 'gzip -9' 'brotli -q11'
	@for f in site/assets/farga.css site/assets/farga.all.css; do \
		printf '%-16s %9sB %9sB %11sB\n' "$$(basename $$f)" \
			"$$(wc -c < $$f | tr -d ' ')" \
			"$$(gzip -9 -c $$f | wc -c | tr -d ' ')" \
			"$$(brotli -q 11 -c $$f | wc -c | tr -d ' ')"; \
	done

open:
	open site/index.html

farga.css:
	sass --style=compressed ./scss/main.scss ./site/assets/farga.css

farga.all.css:
	sass ./scss/all.scss ./site/assets/farga.all.css

clean:
	rm ./site/assets/farga.css
