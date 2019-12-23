PROJECT_NAME := python-banner
PROJECT_VERSION := $(shell python3 setup.py --version)

SHELL := /bin/bash
BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

.PHONY: all
all: uninstall install clean

.PHONY: develop
develop:
	@make clean
	@echo -e "$(BOLD)installing in develop mode $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	dephell deps convert
	cd ..; pipx install -e $(PROJECT_NAME)
	@echo -e -n "$(RESET)"

.PHONY: install
install:
	@echo -e "$(BOLD)installing $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	pipx install $(PROJECT_NAME)
	@echo -e -n "$(RESET)"

.PHONY: uninstall
uninstall:
	@echo -e "$(BOLD)uninstalling '$(PROJECT_NAME)'$(RESET)"
	pipx uninstall $(PROJECT_NAME)

.PHONY: dist
dist:
	@echo -e "$(BOLD)packaging $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	poetry build
	@echo -e -n "$(RESET)"

.PHONY: release
release:
	poetry publish

.PHONY: clean
clean:
	@echo -e "$(BOLD)cleaning $(PROJECT_NAME) $(PROJECT_VERSION) repository$(RESET)"
	@rm -rf build dist pip-wheel-metadata $(PROJECT_NAME).egg-info
