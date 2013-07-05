import pkg_resources


try:
    __version__ = pkg_resources.get_distribution(__package__).version
except:
    __version__ = '<unknown>'
