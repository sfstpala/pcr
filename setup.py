import os.path
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "DESCRIPTION.rst")) as f:
    long_description = f.read()

setuptools.setup(
    name="pcr",
    version="0.8.0",
    license="GPLv3",
    packages=setuptools.find_packages(),
    test_suite="pcr.tests",
    install_requires=[],
    description="Python 3 Cryptography Toolkit",
    long_description=long_description,
    platforms="all",
    author="Stefano Palazzo",
    author_email="stefano.palazzo@gmail.com",
    url="https://github.com/sfstpala/pcr/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: " +
        "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Security :: Cryptography",
    ],
)
