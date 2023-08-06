from distutils.util import strtobool

def _bool(string):
    return bool(strtobool(str(string).strip()))