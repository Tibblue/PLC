# SHELL = /bin/bash

run:
	@ python3 -m diretor.diretor

# make runFile file=[filename]
runFile:
	@ python3 -m diretor.diretor -f $(file)

checkBots:
	python3 -m diretor.bot_tradutor.bot_tradutor
	python3 -m diretor.bot_lista.bot_lista


# wow = ola
# test:
# 	echo $(wow) $(arg)