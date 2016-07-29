## player.py
## В этом файле будет располагаться класс, в котором
##  будет описан класс для сущности "Игрок"

MIN_PLAYER_ID = 1
MAX_PLAYER_ID = 1000000

CROSS_MARK_TYPE = 1
NOUGHT_MARK_TYPE = 0
import random

class Player:
	""" Класс для работы с пользователем. """
	# model = namedtuple("model" , ["player_id", "player_name", "type_of_mark", "is_winner"])
	# 
	

	def __init__(self, name = None, type_of_mark = None):
		self.player_id = random.choice(range(MIN_PLAYER_ID, MAX_PLAYER_ID))
		if not type_of_mark:
			self.type_of_mark = random.randint(NOUGHT_MARK_TYPE, CROSS_MARK_TYPE)
		else:
			self.type_of_mark = type_of_mark

		self.player_name = name


	@property
	def is_winner(self): 
		return self._is_winner


	@is_winner.setter
	def is_winner(self, new_arg):
		self._is_winner = new_arg

		