.PHONY: build run test test-dev shell

build:
	@docker-compose build props

run: build
	@docker-compose run --rm props

test: build
	@docker-compose run --rm props ./scripts/test.sh

test-dev: build
	@docker-compose run --rm props ./scripts/entr.sh

shell: build
	@docker-compose run --rm props sh
