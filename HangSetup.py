import random
from sys import exit
from HangUtil import print_msg


class HangSetup:
	def __init__(self, file):
		self.file = file
		self.total_words = 0
		self.rand_line = 0
		self.the_word = ""


	def open_file(self):
		try:
			self.file = open(self.file, 'r')
		except:
			print_msg("Fatal", self.file + " not found... Exiting program")
			sys.exit()

	def close_file(self):
		self.file.close()

	def set_total_words(self):
		for line in self.file:
			self.total_words +=1

	def get_total_words(self):
		return self.total_words

	def set_rand_line(self):
		self.rand_line = random.randint(0, self.total_words)

	def get_rand_line(self):
		return self.rand_line

	def set_word(self):
		self.file.seek(0)
		current_line = 0
		for line in self.file:
			if current_line == self.rand_line:
				self.the_word = line
				break
			else:
				current_line += 1
		#testing
		self.the_word = 'ftest'

	def get_word(self):
		return self.the_word