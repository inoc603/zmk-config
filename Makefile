all: build_in_docker glv80.svg

glv80.svg: config keymap_config.yaml
	poetry run keymap -c keymap_config.yaml parse -z config/glove80.keymap > glv80.yaml
	poetry run keymap -c keymap_config.yaml draw glv80.yaml > $@
	rm glv80.yaml

setup:
	-poetry run west init -l config
	poetry run west update

build_in_docker:
	docker run -it --rm -v $(shell pwd):/app -w /app zmkfirmware/zmk-build-arm:stable make build -j2

board/%:
	west build -s zmk/app -b "$*" -d build/$* -- \
		-DZMK_CONFIG=$(shell pwd)/config
	cp build/$*/zephyr/zmk.uf2 build/$*.uf2


.PHONY: build
build: 
	west zephyr-export
	$(MAKE) board/glove80_lh board/glove80_rh

format:
	poetry run ruff format scripts
	poetry run python scripts/format_layout.py

upload:
	sudo python scripts/upload.py
