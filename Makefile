all: build/ pcr.egg-info/
build/:
	@python3 setup.py build_ext
pcr.egg-info/:
	@python3 setup.py egg_info

dist:
	@python3 setup.py sdist

test:
	@python3 setup.py test
	@pep8 .

ifdef DEB_HOST_ARCH
DESTDIR ?= /
PREFIX ?= usr/
install:
	@python3 setup.py install --no-compile --prefix="$(PREFIX)" --root="$(DESTDIR)" --install-layout=deb
endif

clean:
	@rm -rfv dist/ build/ pcr.egg-info/
	@find -depth -name "__pycache__" -type d -exec rm -rfv {} \;

.PHONY : dist test clean
