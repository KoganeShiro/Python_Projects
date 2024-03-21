# character generator

character generator for this project...to build an automated game battle system!

Add return functions to your character's health and strength statuses from Day 27's project.
Generate two different characters and store their data (health and strength stats, character type, name, etc.).
Use a while True loop to simulate those two characters battling.
Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
Find the difference between the strength of both opponents and add one.
Take that amount away from the loser's health.
At the end of each round, check the stats of each character to ensure neither of them have died yet.
When one character dies (they run out of health), declare a winner of the battle!
To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
