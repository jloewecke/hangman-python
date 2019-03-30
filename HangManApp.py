from HangSetup import HangSetup
from HangGame import HangGame


def setup_game(MyFile):
	MyFile.open_file()
	MyFile.set_total_words()
	MyFile.set_rand_line()
	MyFile.set_word()


def main():
	MyFile = HangSetup("hangman.txt")
	setup_game(MyFile)
	MyGame = HangGame(MyFile.the_word,10)
	MyGame.init_answer()
	#print(MyGame.word +" - "+ str(MyGame.max_turns))

	while True:
		MyGame.display_answer()
		MyGame.set_letter()
		MyGame.set_guessed_letters()
		MyGame.check_letter()
		if MyGame.check_game_end():
			break


if __name__ == '__main__':
	main()
