## Главный модуль игры, в котором происходит её запуск

import game
import player
import stat
import graphics

DEFAULT_CFG = 'default.py'


class Main:
	"""Класс для запуска игры, объединяющий все остальное"""
	def __init__(self, *, config=DEFAULT_CFG):
		pass

game = Main()