.PHONY: install

install:
	./tools/install.sh
	./tools/install_hooks.sh

migrate:
	./tools/migrate.sh

run_server_dev:
	./tools/run_server_dev.sh

run_tests:
	./tools/run_tests.sh
