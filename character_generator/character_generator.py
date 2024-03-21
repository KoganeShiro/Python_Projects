import random, os
from time import sleep


def rollDice(side):
  result = random.randint(1, side)
  return result


def health():
  health_stat = ((rollDice(6) * rollDice(12)) / 2) + 10
  return health_stat


def strength():
  strength_stat = ((rollDice(6) * rollDice(8)) / 2) + 12
  return strength_stat


creat_again = "yes"

while creat_again == "yes":
  print("Character Builder\n\n")
  sleep(1)
  player_name = input("Name Your Legend:\n")
  player_name = player_name.capitalize()
  oc_type = input(
    "\nCharacter Type:\n (Humaine, Elf, Wizard, Orc, Therianthropy)\n")
  oc_type = oc_type.capitalize()
  sleep(1)
  print("\n", player_name, "\n", oc_type, "\n")
  sleep(1)
  player_health = ""
  player_health = health()
  print("HEALTH:", player_health)
  sleep(1)
  player_strength = ""
  player_strength = strength()
  print("\nSTRENGTH:", player_strength, "\n\n")
  sleep(1)
  creat_again = input("Do you want to creat your character again ? (yes/no) ")
  if creat_again == "yes":
    os.system("clear")
  else:
    print()
    break

enemy_name = input("What's the name of your sworn enemy ? ")
enemy_name = enemy_name.capitalize()
print(enemy_name)
enemy_health = ""
enemy_health = health()
print("HEALTH:", enemy_health)
sleep(1)
enemy_strength = ""
enemy_strength = strength()
print("STRENGTH:", enemy_strength, "\n\n")
sleep(1)
os.system("clear")


def roll_dice():
  roll_result = random.randint(1, 6)
  return roll_result


roll_result = roll_dice()
enemy_roll_result = roll_dice()
''''def player_stat():
  print(player_name)
  print(player_health)
  print(player_strength)
  return (player_stat)

player_stat = player_stat()


def enemy_stat():
  print(enemy_name)
  print(enemy_health)
  print(enemy_strength)
  return (enemy_stat)

enemy_stat = enemy_stat()

ça ne marche pas error : <function player_stat at 0x7f3882ab7430> <function enemy_stat at 0x7f3882ab74c0> '''

round = 1

print("⚔️ BATTLE TIME ⚔️")
print("The battle begins !")

while True:
  sleep(1)
  print(player_name, "roll the dice and obtain", roll_result, '!')
  sleep(1)
  print(enemy_name, "roll the dice and obtain", enemy_roll_result, '!\n')
  sleep(1)

  if roll_result < enemy_roll_result:
    print(enemy_name, "wins the", round, "round !", player_name,
          "takes a hit with", enemy_strength, "damage !!")
    sleep(1)
    player_health -= enemy_strength
    print(
      f"\n{player_name}\nHealth :{player_health}\nStrength : {player_strength}"
    )
    sleep(1)
    print(
      f"\n{enemy_name}\nHealth : {enemy_health}\nStrength : {enemy_strength}")
    sleep(1)
    continued = input("\nEnter anything to continue !")

  elif roll_result > enemy_roll_result:
    print(player_name, "wins the", round, "round !", enemy_name,
          "takes a hit with", player_strength, "damage !!\n")
    sleep(1)
    enemy_health -= player_strength
    print(
      f"\n{player_name}\nHealth :{player_health}\nStrength : {player_strength}"
    )
    sleep(1)
    print(
      f"\n{enemy_name}\nHealth : {enemy_health}\nStrength : {enemy_strength}")
    sleep(1)
    continued = input("\nEnter anything to continue !")

  else:
    print("\nThat's a drawn round !\n")
    sleep(1)
    continued = input("\nEnter anything to continue !")
    continue

  if player_health > 0 and enemy_health > 0:
    sleep(1)
    print("\nAnd they're both standing for the next round!")
    os.system("clear")
    round += 1
    print("⚔️ BATTLE TIME ⚔️")
    print("The battle continues !")
    continue

  if player_health < 0:
    print("\nOh no", player_name, "has died !")
    sleep(1)
    print(f"{enemy_name} destroyed {player_name} in {round} round !")
    break

  if enemy_health < 0:
    print("\nOh no", enemy_name, "has died !")
    sleep(1)
    print(f"{player_name} destroyed {enemy_name} in {round} round !")
    break

