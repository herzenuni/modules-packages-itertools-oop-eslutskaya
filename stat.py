## stat.py
## В этом файле будет располагаться класс, в котором
##  будет описан класс для сущности "Статистика" (таблица результатов)

class Table_Of_Results:
	""" Класс для работы с таблицей результатов. 

	Данный класс будет позволять 
	 - считывать результаты из файла,
	 - записывать в файл результат, 
	 - показать последний результат.
	"""
	
	result = " " #should be named tuple

	results_table  = " "

	def __init__(self, result):
		"""конструктор класса"""
		self.result = result

	def get_results_from_file(self, file):
		"""получить все результаты из файла""" 
		return results_table

	def write_result_to_file(self, result):
		"""записать результат в файл""" 


	def show_result(self, *, show_all=False):
		
		return results_table
