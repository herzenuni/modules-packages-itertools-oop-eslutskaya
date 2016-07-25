## player.py
## В этом файле будет располагаться класс, в котором
##  будет описан класс для сущности "Игрок"

MIN_PLAYER_ID = 1
MAX_PLAYER_ID = 1000000
import random

class Player:
	""" Класс для работы с пользователем. """
	# model = namedtuple("model" , ["player_id", "player_name", "type_of_mark"])


	def __init__(self, *, name = None, type_of_mark = "cross"):
		self.player_id = random.choice(range(MIN_PLAYER_ID, MAX_PLAYER_ID))
		self.player_name = name

# new_player1 = Player(name = "Nick", type_of_mark = "cross")
# new_player2 = Player(name = "Paul", type_of_mark = "nought")