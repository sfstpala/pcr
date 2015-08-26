python = python3.4

all: pcr.egg-info

pcr.egg-info: setup.py bin/pip bin/wheel
	bin/pip install --editable . && touch $@
bin/pip: bin/python
	curl https://bootstrap.pypa.io/get-pip.py | bin/python
bin/wheel: bin/pip
	bin/pip install wheel
bin/python:
	$(python) -m venv --without-pip .

test: all bin/coverage bin/flake8 bin/check-manifest bin/rst2xml.py
	bin/coverage run setup.py test
	bin/coverage html
	bin/coverage report
	bin/flake8 setup.py pcr
	bin/check-manifest
	bin/python setup.py check -mrs
bin/coverage: bin/pip
	bin/pip install coverage
bin/flake8: bin/pip
	bin/pip install flake8
bin/check-manifest: bin/pip
	bin/pip install check-manifest
bin/rst2xml.py: bin/pip
	bin/pip install docutils

docs: all bin/pdoc bin/pygmentize setup.py
	bin/pdoc --html --only-pypath --html-dir ./docs --overwrite pcr pcr
bin/pdoc: bin/pip
	bin/pip install pdoc
bin/pygmentize: bin/pip
	bin/pip install pygments

doctest: all
	bin/python -m doctest README.md

wheels: bin/wheel all
	bin/pip wheel .

clean:
	rm -rf docs build dist $(shell find pcr -name "__pycache__")
	rm -rf *.egg-info *.egg bin lib lib64 include share pyvenv.cfg
	rm -rf wheelhouse htmlcov .coverage .tox pip-selfcheck.json
