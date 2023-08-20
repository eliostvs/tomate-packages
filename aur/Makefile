ifeq ($(origin .RECIPEPREFIX), undefined)
	$(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif

.DEFAULT_GOAL = help
.DELETE_ON_ERROR:
.ONESHELL:
.SHELLFLAGS   := -euo pipefail -c
.SILENT:
MAKEFLAGS     += --no-builtin-rules
MAKEFLAGS     += --warn-undefined-variables
SHELL         = bash

DOCKER_IMAGE  = eliostvs/aur
DOCKER_HOME   = /home/pkg/code
DOCKER_MARKER = .dockermarker
release       ?= 1
name          ?= ""

guard-%:
	if [ "${${*}}" = "" ]; then \
    	echo "Environment variable $* not set"; \
    	exit 1; \
	fi

## help: print this help message
help:
	echo 'Usage:'
	sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /' | sort
.PHONY: help


${DOCKER_MARKER}: clean docker
	# docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -t ${DOCKER_IMAGE} .
	# touch ${DOCKER_MARKER}

## clean: delete environment
clean:
	rm ${DOCKER_MARKER} 2> /dev/null || true
.PHONY: clean

## docker: build the docker image
docker:
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -t ${DOCKER_IMAGE} .
	touch ${DOCKER_MARKER}
.PHONY: docker

## arch: start archlinux docker image
arch: ${DOCKER_MARKER}
	docker run --network=host --rm -it -v $(CURDIR):$(DOCKER_HOME) --workdir $(DOCKER_HOME) $(DOCKER_IMAGE) bash
.PHONY: arch

## delete <name>: delete package from disk
delete: guard-name
	rm -rf ${name} 2> /dev/null || true
.PHONY: delete

## clone <name>: clone pacakge metadata from aur registry
clone: guard-name
	rm -rf ${name}
	git clone "ssh://aur@aur.archlinux.org/${name}.git"
.PHONY: clone

## package <name> <version> <release>: update package metadata version/release
package: guard-name guard-version guard-release
	pushd ${name}
	echo "Update package ${name} to version ${version}-${release}"
	sed -i "s|pkgver=[0-9]*.[0-9]*.[0-9]*|pkgver=${version}|" PKGBUILD
	sed -i "s|pkgrel=[0-9]|pkgrel=${release}|" PKGBUILD
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO
	popd
.PHONY: package

## release <name> <version> <release>: save package metadata and push changes to aur registry
release: guard-name guard-version guard-release
	pushd ${name}
	git commit -am "Update version to ${version}-${release}"
	git push -u origin master
	popd
.PHONY: release

## updatesums <name> <version> <release>: update package metadata using docker
updatesums: ${DOCKER_MARKER} guard-name guard-version guard-release
	docker run --rm -v ${CURDIR}:${DOCKER_HOME} --workdir ${DOCKER_HOME} -e name=${name} -e version=${version} -e release=${release} ${DOCKER_IMAGE} make package
.PHONY: updatesums

