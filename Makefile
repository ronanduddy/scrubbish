.PHONY: build run test test-dev shell lint

build:
	@docker-compose build scrubbish

run: build
	@docker-compose run --rm scrubbish

test: build
	@docker-compose run --rm scrubbish ./scripts/test.sh

test-dev: build
	@docker-compose run --rm scrubbish ./scripts/entr.sh

shell: build
	@docker-compose run --rm scrubbish sh

lint: build
	@docker-compose run --rm scrubbish black .
