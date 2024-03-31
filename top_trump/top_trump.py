#top trumps game !
import random, os

card_dictionary = []
deck1 = []
deck2 = []

def display_card(card):
    print("NAME:", card["NAME"])
    print("HP:", card["HP"])
    print("ATK:", card["ATK"])
    print("MP:", card["MP"])
    print()

def create_card(name, HP, ATK, MP):
    card = {
        "NAME": name,
        "HP": HP,
        "ATK": ATK,
        "MP": MP
    }
    return card

# Create cards with the name that you want
card1 = create_card("Card 1", 100, 10, 5)
card2 = create_card("Card 2", 80, 15, 10)
crad3 = create_card("Card 3", 120, 8, 3)
card4 = create_card("Card 4", 90, 12, 7)
card5 = create_card("Card 5", 110, 9, 4)

# Add cards to decks
deck1 = [card1]
deck2 = [card2]

# Play the game
player_score = 0
computer_score = 0

while True:
    print("Computer's turn:")
#    display_card(deck1[0])

    print("Player's turn:")
    display_card(deck2[0])

    chosen_stat = input("Choose a stat to compare (NAME, HP, ATK, MP)\n").upper()

    if chosen_stat in deck1[0] and chosen_stat in deck2[0]:
        if deck1[0][chosen_stat] > deck2[0][chosen_stat]:
            computer_score += 1
            display_card(deck1[0])
            display_card(deck2[0])
            print("Computer wins this round!")
        elif deck1[0][chosen_stat] < deck2[0][chosen_stat]:
            player_score += 1
            display_card(deck1[0])
            display_card(deck2[0])
            print("Player wins this round!")
        else:
            print("It's a tie!")

    print("Computer Score:", computer_score)
    print("Player Score:", player_score)

    play_again = input("Do you want to play another round? (yes/no): ")
    os.system("clear")
    if play_again.lower() != "yes":
        break

print("Final Scores: ")
print("Computer Score: ", computer_score)
print("Player Score: ", player_score)
if computer_score > player_score:
    print("Player wins!")
elif computer_score < player_score:
    print("Computer wins!")
else:
    print("It's a tie!")
