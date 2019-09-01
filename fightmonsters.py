import random
import time
from time import sleep

name = input("Welcome to the adventure!  Enter your new character's name:")
print ("Your new characters is named " + name)
strength = random.randint(0,3)
dexterity = random.randint(0,3)
constitution = random.randint(0,3)
hitpoints = random.randint(5,10) + constitution

print ("Here are your stat modifiers:")
sleep(1)
print ("Strength: " + str(strength))
sleep(1)
print ("Dexterity: " + str(dexterity))
sleep(1)
print ("Constitution: " + str(constitution))
sleep(1)
print ("Hit Points: " + str(hitpoints))
sleep(2)

goblinkills = 0
spiderkills = 0
xp = 0

print ("\nYou enter the dungeon!")

def fightmonster(monster="", monstermaxhp=1, monsterac = 10, monsterxp=0, monsterdamage=1, hitpoints=0, kills=0, xp=0):
	# This is a generic fight function, you can tell it what to fight
	monsterhp = random.randint(1,monstermaxhp)
	print ("You see a " + monster + "!")
	print ("It has " + str(monsterhp) + " hit points!")
	while monsterhp > 0 or hitpoints > 1:
		print ("Do you want to attack? (y/n)")
		attack = raw_input()
		if attack == 'y':
			print ("You try and hit the " + monster+ "!")
			tohit = random.randint(1,20)
			print ("You roll a " + str(tohit) + "!!!!")
			if tohit > monsterac:
				print ("You hit the " + monster + "!")
				damage = random.randint(1,12) + strength
				monsterhp = monsterhp - damage
				if monsterhp < 1:
					print ("You killed the " + monster + "!")
					kills = kills + 1
					xp = xp + monsterxp

				else:
					print("You hit for " + str(damage) + ", the " + monster + ", it has " + str(monsterhp) + " hit points left")
			else:

				print ("Your pitiful attempt fails!  You miss the " + monster + "!")
		print ("The " + monster + " tries to smite you!")


		if random.randint(1,20) > 10 + dexterity:
			damage = random.randint(1,monsterdamage)
			print ("The " + monster + " hits you for " + str(damage) + " damage!")
			hitpoints = hitpoints - damage
			print ("You have " + str(hitpoints) + " hit points left!")
		else:
			print ("The goblin misses you!")
	return [hitpoints, kills, xp]

def fightspider(hitpoints = 0, spiderkills = 0, xp = 0):
	#put the spider fighting code in here
	return [hitpoints, spiderkills, xp]

def fightgoblin(hitpoints = 0, goblinkills=0, xp=0):
	[hitpoints, goblinkills, xp] = fightmonster("goblin", 10, 12, 25, 6, hitpoints, goblinkills, xp)
	return [hitpoints, goblinkills, xp]
	
while hitpoints > 0:
	randmonster = random.randint(1,3)
	if randmonster == 1:
		print ("You encounter a goblin!")
		[hitpoints, goblinkills, xp] = fightgoblin(hitpoints, goblinkills, xp)
		print ("You have killed " + str(goblinkills) + " goblins!")
	elif randmonster == 2:
		print ("You encounter a spider!")
		[hitpoints, spiderkills, xp] = fightspider(hitpoints, spiderkills, xp)
		print ("You have killed " + str(spiderkills) + " goblins")
	else:
		print ("You wander the dungone for a while...")
	
print ("Sorry, you died! But you killed " + str(goblinkills) + " goblins!")
print ("You also killed " + str(spiderkills) + " spiders.")
print ("\n so there's that...")

