import setuptools


setuptools.setup(
    name="pcr",
    version="0.7.0",
    license="GPLv3",
    packages=setuptools.find_packages(),
    test_suite="pcr.tests",
    install_requires=[],
    description="Python 3 Cryptography Toolkit",
    long_description=(
        "A cryptography toolkit implemented in pure python 3. PCR includes "
        "AES, CBC (mode of operation), Diffie-Hellman, HOPT (two-factor-"
        "authentication), pbkdf2 (key derivation), RC4, and XTEA, as well "
        "as some ancillary modules."),
    platforms="all",
    author="Stefano Palazzo",
    author_email="stefano.palazzo@gmail.com",
    url="https://github.com/sfstpala/pcr/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: " +
        "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Security :: Cryptography"],
)
