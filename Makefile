.PHONY: test lint-check lint-fix

test:
	python -m pytest tests -vvv

lint-check:
	black --check --diff app
	autoflake --check -ri --ignore-init-module-imports --remove-all-unused-imports app
	mypy -p app

lint-fix:
	black app tests
	autoflake -ri --ignore-init-module-imports --remove-all-unused-imports app tests
	mypy -p app
