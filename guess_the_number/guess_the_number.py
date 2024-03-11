import random
import time

def get_player_name():
    print("Hey! What's your name, buddy?")
    return input()

def generate_random_number():
    return random.randint(1, 1000)

def guess_number():
    return int(input("Can you guess it?\n"))

def provide_hint(secret_number, guess):
    if guess < secret_number:
        print("Nope, but I'll give you a hint! It's bigger ;)")
    elif guess > secret_number:
        print("Nope, but I'll give you a hint! It's smaller ^^")

def main():
    guesses_taken = 0
    player_name = get_player_name()
    secret_number = generate_random_number()

    print(f"Ok {player_name}! I'm thinking about a number right now.")

    for guesses_taken in range(6):
        player_guess = guess_number()

        if player_guess == secret_number:
            break
        else:
            provide_hint(secret_number, player_guess)

    if player_guess == secret_number:
        guesses_taken += 1
        print(f"Congratulations {player_name}! You guessed it right!")
        print(f"With a total of {guesses_taken} try(s) >w<")
    else:
        secret_number = str(secret_number)
        print(f"What a shame... My number was {secret_number} T_T")

    print()
    time.sleep(5)

if __name__ == "__main__":
    main()

