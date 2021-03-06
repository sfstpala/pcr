# Copyright (c) 2013 Stefano Palazzo <stefano.palazzo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

python = python3

all: pcr.egg-info

pcr.egg-info: setup.py bin/pip bin/wheel
	bin/pip install --editable . && touch $@
bin/pip: bin/python
	curl https://bootstrap.pypa.io/get-pip.py | bin/python
bin/wheel: bin/pip
	bin/pip install wheel
bin/python:
	$(python) -m venv --without-pip .

test: all bin/coverage bin/pylama bin/check-manifest bin/rst2xml.py
	bin/coverage run setup.py test
	bin/coverage html
	bin/coverage report
	bin/pylama setup.py pcr
	bin/check-manifest
	bin/python setup.py check -mrs
bin/coverage: bin/pip
	bin/pip install coverage
bin/pylama: bin/pip
	bin/pip install pylama
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
	bin/pip wheel -w wheelhouse .

clean:
	rm -rf docs build dist $(shell find pcr -name "__pycache__")
	rm -rf *.egg-info *.egg bin lib lib64 include share pyvenv.cfg
	rm -rf wheelhouse htmlcov .coverage .tox pip-selfcheck.json
