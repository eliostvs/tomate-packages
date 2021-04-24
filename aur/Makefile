ifeq ($(origin .RECIPEPREFIX), undefined)
	$(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif

.DELETE_ON_ERROR:
.ONESHELL:
.SHELLFLAGS   := -euo pipefail -c
.SILENT:
MAKEFLAGS     += --no-builtin-rules
MAKEFLAGS     += --warn-undefined-variables
SHELL         = bash

DOCKER_IMAGE  = eliostvs/aur
DOCKER_HOME   = /home/pkg/code
release       ?= 1

.PHONY: clone
clone:
	rm -rf $(name)
	git clone ssh://aur@aur.archlinux.org/$(name).git

.PHONY: docker
docker:
	docker rmi $(DOCKER_IMAGE) 2> /dev/null || true
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -t $(DOCKER_IMAGE) .

.PHONY: run
run:
	# in the host run the command `xhost +` then in the container open an app with the command `DISPLAY=:0 app`
	docker run --network=host --rm -it -v $(CURDIR):$(DOCKER_HOME) --workdir $(DOCKER_HOME) $(DOCKER_IMAGE) bash

.PHONY: update
update:
	docker run --rm -v $(CURDIR):$(DOCKER_HOME) --workdir $(DOCKER_HOME) -e name=$(name) -e version=$(version) -e release=$(release) $(DOCKER_IMAGE) make pkg

.PHONY: pkg
pkg:
	cd $(name)
	echo "Update package $(name) to version $(version)-$(release)"
	sed -i "s|pkgver=[0-9]*.[0-9]*.[0-9]*|pkgver=$(version)|" PKGBUILD
	sed -i "s|pkgrel=[0-9]|pkgrel=$(release)|" PKGBUILD
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO

.PHONY: commit
commit:
	cd $(name)
	git clean -fd
	git commit -am "Update version to $(version)-$(release)"
	git push
