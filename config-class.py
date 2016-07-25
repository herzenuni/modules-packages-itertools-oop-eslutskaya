## Файл конфига
from collections import namedtuple
Config = namedtuple("Config", ["whos_turn", "field_size", "path_to_stat_file", "window_size"])

class Config(object):
	"""docstring for Config"""
	def __init__(self, arg):
		super(Config, self).__init__()
		self.arg = arg



## main 

DEFAULT_CFG = config.py


def __init__(self, *, config = DEFAULT_CFG)