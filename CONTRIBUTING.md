# Contributing to PCR

## Tests

Note that each module in PCR needs to have a unit test (in
`pcr/test/test_*.py`), which must cover the entirety of the
functionality provided.

If at all possible, use NIST or IETF test vectors to test
standardised cryptographic algorithms.

## Style

The arguments used for the functions should be reasonably
low-level (i.e. do not abstract away any of the parameters
specificed for the algorithm), but they must not be confusing.

When in doubt, use argument annotations to specify types
and comments (such as the ones in pbkdf2.py) to explain any
argument. Do provide reasonable defaults.

Furthermore, all code must pass pep8 without exception.

## License

All code in PCR is licensed under the terms of the GNU
General Public License (version 3 or later). You may add
your name at the top of the file when you change it (do
however follow the style used in the file). Please also
edit `debian/copyright` in the same way.
