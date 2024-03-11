import random

HANGMAN_PICS = [
    '''
    ===''',
    '''
     |
     |
     |
    ===''',
    '''
+-----+
     |
     |
     |
    ===''',
    '''
+-----+
 0   |
     |
     |
    ===''',
    '''
+-----+
 0   |
 |   |
     |
    ===''',
    '''
+-----+
 0   |
/|   |
     |
    ===''',
    '''
+-----+
 0   |
/|\  |
     |
    ===''',
    '''
+-----+
 0   |
/|\  |
/    |
    ===''',
    '''
+-----+
 0   |
/|\  |
/ \  |
    ==='''
]

words = [
  "apple", "banana", "orange", "grape", "strawberry", "melon", "kiwi", "pineapple", "peach", "plum",
  "computer", "keyboard", "mouse", "monitor", "laptop", "printer", "router", "tablet", "smartphone", "headphones",
  "ocean", "mountain", "river", "forest", "desert", "valley", "canyon", "waterfall", "lake", "island",
  "sunflower", "daisy", "rose", "tulip", "lily", "daffodil", "carnation", "orchid", "iris", "poppy",
  "guitar", "piano", "violin", "trumpet", "drums", "saxophone", "flute", "harmonica", "clarinet", "accordion",
  "book", "novel", "magazine", "newspaper", "dictionary", "encyclopedia", "biography", "fiction", "nonfiction", "poetry",
  "car", "bicycle", "motorcycle", "bus", "train", "airplane", "ship", "helicopter", "submarine", "rocket",
  "happy", "sad", "excited", "bored", "angry", "surprised", "calm", "anxious", "confused", "content",
  "sun", "moon", "star", "cloud", "rain", "snow", "wind", "thunderstorm", "lightning", "rainbow",
  "coffee", "tea", "juice", "water", "soda", "milk", "smoothie", "wine", "beer", "cocktail"
]

def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Incorrect letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    while True:
        print("\n\nGuess a letter: ")
        guess = input().lower()
        if len(guess) != 1:
            print("Please enter only one letter at a time.")
        elif guess in already_guessed:
            print("You've already guessed that letter!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter a LETTER, not something else.")
        else:
            return guess


def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


print("H A N G M A N")
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess
        found_all_letters = all(letter in correct_letters for letter in secret_word)

        if found_all_letters:
            print(f'Yes! The secret word is "{secret_word}"! You won!')
            game_is_done = True
    else:
        missed_letters += guess

        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f'You\'ve run out of guesses!\nAfter {len(missed_letters)} incorrect letters and {len(correct_letters)} correct letters, the secret word was "{secret_word}".')
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break

