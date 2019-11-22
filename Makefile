## Constants
PWD := $(shell pwd)
VOLUME_NOTEBOOKS := $(PWD)/analysis
HOST_NOTEBOOKS := /home/jovyan

## Docker
jupyter:
    docker run -p 8888:8888 \
	    -v $(VOLUME_NOTEBOOKS):$(HOST_NOTEBOOKS) jupyter/minimal-notebook:latest

## Preparing
build:mkdir-notebooks

## Auxiliary Commands
mkdir-%:
	mkdir -p $(PWD)/$*
	chmod a+w $(PWD)/$*