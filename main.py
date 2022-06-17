import random
from replit import clear

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel", "happy", "india", "paris"]
chosen_word = random.choice(word_list)

display = []
length = len(chosen_word)

lives = 6

for x in chosen_word:
    display.append("_")
print(display)
right = 0
while right != length:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print("****The letter is already guessed****")
        print("******Please enter other letter******")
        print(display)
        print(stages[lives])
    else:

        a = 0
        i = 0
        for letter in chosen_word:
            if letter == guess:
                display[i] = letter
                print("----Great Guess!!----")
                right = right + 1
            else:
                a = a + 1
            i = i + 1
        if a == len(chosen_word):
            lives = lives - 1
            print("----Thats a worng guess. You lose a life.----")
        print(display)
        print(stages[lives])

        if lives == 0:
            print("------You Have Lost------")
            print(f'The word was either "{chosen_word}"')
            break
        continue
if right == len(chosen_word):
    print("----Contratulations! You have won.----")
