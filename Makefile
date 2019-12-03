## Constants
PWD := $(shell pwd)
VOLUME_NOTEBOOKS := $(PWD)/analysis
HOST_NOTEBOOKS := /home/jovyan
IMAGE := game-recommender
PORT := 8888

## Docker
jupyter: 
	docker run -p $(PORT):$(PORT) \
	-v $(VOLUME_NOTEBOOKS):$(HOST_NOTEBOOKS) jupyter/minimal-notebook:latest

## Application
run:
	@ echo "GAMER RECOMMENDING SYSTEM"
	@ docker run -it $(IMAGE)

## Preparing
build:
	@ echo "CREATE DOCKER IMAGE"
	@ docker build -t $(IMAGE) .

## Auxiliary Commands
mkdir-%:
	mkdir -p $(PWD)/$*
	chmod a+w $(PWD)/$*