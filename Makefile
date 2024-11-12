test:
	python -m pytest tests

package: test
	python scripts/package_examples.py

