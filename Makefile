launch:
	docker run -it --rm \
	  -p 127.0.0.1:8888:8888 \
	  --name ml-workshop \
	  --user=root \
	  -e NB_UID=$(shell id -u) -e NB_GID=$(shell id -g) \
	  -v "$(shell pwd):/home/jovyan/work" \
	  jupyter/scipy-notebook
