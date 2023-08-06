try:
    from .main import *
    from .utils import *
except SyntaxError:
    pass
except ModuleNotFoundError:
    pass

NAME = "mol2grid"
VERSION = "0.1.1"
LICENSE = "GNU GPL-3.0 License"
