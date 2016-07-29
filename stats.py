## Stats.py
## В этом файле будет располагаться класс, в котором
##  будет описана сущность "Статистика" (таблица результатов)
from collections import namedtuple
import csv


class Stats:
	""" Класс для работы с таблицей результатов. 
	Прежнее название 'Table of results'

	Данный класс будет позволять 
	 - считывать результаты из файла,
	 - записывать в файл результат, 
	 - показать последний результат.
	"""
	Result = namedtuple("Result", ["game_id", "winner_id", "player1_name", "player2_name", "winner_name", "game_time", "type_of_mark"])
	

	results_table = []
	file = None


	def __init__(self, file):
		"""конструктор класса"""
		Stats.file = file


	def get_results_from_file(self):
		"""получить все результаты из файла""" 
		try:
			with open(Stats.file, newline="") as csvfile:
				csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				for row in csvreader:
					result = Result(row[0], row[1], row[2], row[3])
					Stats.results_table.append(result)

		except FileNotFoundError:
			print ("File with results table ({})  was not found.\r".format(Stats.file))
			print ("Creating new file {}".format(Stats.file))
			fp = open(Stats.file, 'a+')
			Stats.results_table = None

		return Stats.results_table


	def write_result_to_file(self, new_result = None):
		"""записать результат в файл""" 
		if not new_result:
			self.new_result = new_result
			if not Stats.file:
				try:
					with open(Stats.file, 'a+', newline="") as csvfile:
						csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
						csvwriter.writerow(self.new_result)
						return self.new_result
				except IOError:
					return "Input/output error with new result {}".format(self.new_result)



	def print_result(self, *, result_id = None, print_all = False):
		if result_id and not print_all:
			print(self.new_result.winner_id, self.new_result.winner_name, self.new_result.game_time, self.new_result.type_of_mark)
		# TODO
		if print_all:
			for el in Stats.results_table:
				print(el.winner_id, el.winner_name, el.game_time, el.type_of_mark)
		return self.new_result

	def get_filename(self):

		return Stats.file


# Result = namedtuple("Result" , ["winner_id", "winner_name", "game_time", "type_of_mark"])
# new_result1 = Result("1", "Ivan", "600", "nought")
# new_result2 = Result("2", "Sveta", "324", "cross")

# new_stat = Stats(file = '1.conf')
# new_stat.get_results_from_file()
# new_stat.write_result_to_file()

# new_stat.print_result(print_all = True)