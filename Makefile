#!/usr/bin/make

IN=spammers.yml
OUT= \
    generated/blacklist.yml \
    generated/blacklist.cfg \
    $(NULL)

all: $(OUT)

generated/blacklist.yml: $(IN)
	./gen_config.py $< --format=ejabberd-yaml --out=$@

generated/blacklist.cfg: $(IN)
	./gen_config.py $< --format=ejabberd-erl --out=$@

