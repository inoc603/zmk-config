glv80.svg: config
	keymap parse -z config/glove80.keymap > glv80.yaml
	keymap draw glv80.yaml > $@
	rm glv80.yaml

setup:
	-poetry run west init -l config
	poetry run west update

build_in_docker:
	docker run -it --rm -v $(shell pwd):/app -w /app zmkfirmware/zmk-build-arm:stable make build

board/%:
	west zephyr-export
	west build -s zmk/app -b "$*" -d build/$* -- \
		-DZMK_CONFIG=$(shell pwd)/config
	cp build/$*/zephyr/zmk.uf2 build/$*.uf2


.PHONY: build
build: board/glove80_lh board/glove80_rh
