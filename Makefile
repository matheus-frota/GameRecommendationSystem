## Constants
PWD := $(shell pwd)
VOLUME_NOTEBOOKS := $(PWD)/analysis
HOST_NOTEBOOKS := /home/jovyan
IMAGE := analysis
PORT := 8888

## Docker
jupyter: 
	docker run -p $(PORT):$(PORT) \
	-v $(VOLUME_NOTEBOOKS):$(HOST_NOTEBOOKS) jupyter/minimal-notebook:latest

## Preparing
build:
	echo "CREATE DOCKER IMAGE"
	docker build -t $(IMAGE) .

## Auxiliary Commands
mkdir-%:
	mkdir -p $(PWD)/$*
	chmod a+w $(PWD)/$*

run:
	python3 ./gameRecommender/main.py

clean:
	sudo python3 setup.py clean --all
	sudo rm -rf *.pyc __pycache__ build dist gameRecommender.egg-info gameRecommender/__pycache__
