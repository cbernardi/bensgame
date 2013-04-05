print "Welcome to the Ben's Game. You choose the path for this story. What's your name?"

name = raw_input("> ")

if name == "Ben" or "Benjamin":
	print "Ahhh, %s, the game maker. Do you dare take your own challenge? Y or N" % name

elif name == "Mila" or "mila":
	print "Hello %s. You are Ben's sister, are you not? Shall we begin? Y or N" % name

else:
	print "Welcome %s. Shall we begin? Y or N" % name

answer = raw_input("> ")

if answer == "Y" or answer == "y":
	print "You're in a neighborhood with four houses. Which house do you choose? 1, 2, 3, 4"

	house = raw_input("> ")

	# house 1
	if house == "1":
		print "The first house is an old mansion. What do you do?"
		print "1. Go inside."
		print "2. Pick another house."

		house1_choice1 = raw_input("> ")

		if house1_choice1 == "1":
			print "Inside is dark and there are two hallways. Which one do you go down?"
			print "1. Go left."
			print "2. Go right."

			house1_choice2 = raw_input("> ")

			if house1_choice2 == "1":
				print "You get sucked into a time portal and find yourself surrounded by lava. You disintegrate. The end."
			else:
				print "At the end of the hallway is a great room with a large table covered in all your favorite foods. Well done!"

		else:
			print "Really? You are changing your mind?! I quit. The end."

	# house 2
	elif house == "2":
		print "The second house is a small cottage. What do you do?"
		print "1. Go inside."
		print "2. Pick another house."

		house2_choice1 = raw_input("> ")

		if house2_choice1 == "1":
			print "Inside its dimly lit and cold and there are two doors. Which one do you choose?"
			print "1. Left door."
			print "2. Right door."

			house2_choice2 = raw_input("> ")

			if house2_choice2 == "1":
				print "You open the left door to find a room filled with treaures. Well done!"
			else:
				print "Behind the right door is more darkness. You step forward and fall in a bottomless pit. The end."

		else:
			print "Really? You are changing your mind?! I quit. The end."

	# house 3
	elif house == "3":
		print "The third house is a brick house. What do you do?"
		print "1. Go inside."
		print "2. Pick another house."

		house3_choice1 = raw_input("> ")

		if house3_choice1 == "1":
			print "Its hot inside and smells like dirt. You see two staircases going up. Which do you choose?"
			print "1. Go left."
			print "2. Go right."

			house3_choice2 = raw_input("> ")

			if house3_choice2 == "1":
				print "As you walk up the left stairs, they begin to shake. Next thing you know, they collapse and you slide in to a pit opf snakes. The end."
			else:
				print "As you walk up the right staircase, the air gets cooler and smells of saltwater. You find yourself sailing away on a boat to your own private island."

		else:
			print "Really? You are changing your mind?! I quit. The end."

	# house 4
	else:
		print "The fourth house is not a house at all. There's a large dark shape coming at you. What do you do?"
		print "1. Run!"
		print "2. Pinch yourself and hope its a dream."

		house2_choice1 = raw_input("> ")

		if house2_choice1 == "1":
			print "You run for your life and escape to live another day. Well done!"
		else:
			print "You pinch yourself only to realize that you are not dreaming and giant is charging at you. The end."

else:
	print "Sorry to hear that %s. Maybe another time." % name



