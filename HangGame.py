from HangUtil import print_row, clear_screen, print_msg


class HangGame:
	def __init__(self, word, max_turns):
		self.word = word
		self.max_turns = max_turns
		self.letter = ''
		self.answer = []
		self.guessed_letters = ''


	def set_letter(self):
		while True:
			try:
				print("\n")
				print("Guess # " + str(len(self.guessed_letters)))
				self.letter = input("Enter a letter from (a-z): ").lower()
				if self.letter < 'a' or self.letter > 'z':
					raise ValueError("Invalid Input - Enter a char between(a-z)")
				if len(self.letter) > 1:
					raise ValueError("Invalid Input - Must be only 1 character")
				break
			except ValueError as ve:
				print_msg("Error", " - " + str(ve))

		if self.letter in self.guessed_letters:
			print_msg("Error", " - You already selected " + self.letter)
			self.set_letter()

	def check_letter(self):
		idx = 0
		new_answer= []
		for char in self.word:
			if char == self.letter:
				new_answer.append(char)
			else:
				new_answer.insert(idx, self.answer[idx])
			idx += 1
		self.answer = new_answer
		self.max_turns -= 1

	def init_answer(self):
		self.answer= []
		for char in self.word:
			self.answer.append('_ ')
	
	def display_answer(self):
		curr_answer = ''
		for item in self.answer:
			curr_answer += item
		clear_screen()
		print_row("Board", "Selected Letters", "Turns Left")
		print_row(curr_answer, str(self.guessed_letters),str(self.max_turns))

	def set_guessed_letters(self):
		self.guessed_letters += self.letter

	def check_game_end(self):
		if self.answer == list(self.word):
			print_msg("Info", "Winner - Congrats you guessed (" +
				self.word +")")
			return True

		if self.max_turns <= 0:
			print_msg("Info", "Loser - The correct answer was (" +
				self.word +")")
			return True