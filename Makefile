glv80.svg: config
	keymap parse -z config/glove80.keymap > glv80.yaml
	keymap draw glv80.yaml > $@
	rm glv80.yaml
