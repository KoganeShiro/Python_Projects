import random
import time

def displayIntro():
    print("Welcome, young traveler to the land of dragons !... In front of you, you have two cave.")
    print("One have a nice dragon inside and will help you and even share his treasure with you")
    print("The other one will eat you without any mercy")
    
def choseCave():
    cave = ""
    while cave != '1' and cave !='2':
        print("So now that you know that...")
        print("Wich cave will you choose ? (1 or 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You slowly and carfully enter the cave")
    time.sleep(2)
    print("It's so dark inside that you cannot see anything when all of sudden !...")
    print("A gigantic dragon appear with his mouth wild open and!...")
    time.sleep(5)
    print()
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print("Congrats you for coming here with a big smile :)")
    else:
        print("You're now a dead meat °-° ")
    print()
    
playAgain = "yes"
while playAgain == "yes" or playAgain == 'o':
    displayIntro()
    caveNumber = choseCave()
    checkCave(caveNumber)
    
    print("Do you want to play again ? (yes or no) ")
    playAgain = input()
    
print()
time.sleep(7)
