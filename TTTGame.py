from TTTLib import *

T = genBoard()

while True:

	#Player "X" (user)

	print(printBoard(T))

	#ensure user input is valid
	
	while True:
		
		Xmove = input("Player X, where would you like to play?\n")

		if (int(Xmove) >= 0) and (int(Xmove) <= 8):
			if T[int(Xmove)] == 0:
				break

			else:
				print("Invalid entry: The slot is already taken.")
				print("Please enter a new number:")

		else:
			print("Invalid entry: The number you entered in out of range.")
			print("Please enter a valid number from 0 to 8:")

	#place X in the indicated slot

	T[int(Xmove)] = 1

	#analyze the game state after X move

	state = analyzeBoard(T)

	if state == 1:
		print(printBoard(T))
		print("Player X wins!")
		break

	if state == 3:
		print(printBoard(T))
		print("Draw")
		break


	#Player "O" (computer)

	print(printBoard(T))
	print("Player O:")

	#place O in the best spot as analyzed by the simulation functions

	while True:
		
		winmove = genWinningMove(T,2)
		if winmove != -1:
			T[int(winmove)] = 2
			break
	
		nonlosemove = genNonLosingMove(T,2)
		if nonlosemove != -1:
			T[int(nonlosemove)] = 2
			break
	
		randmove = genRandomMove(T,2)
		if T[int(randmove)] == 0:
			T[int(randmove)] = 2
			break

	#analyze the game state after O move

	state = analyzeBoard(T)

	if state == 2:
		print(printBoard(T))
		print("Player O wins!")
		break

	if state == 3:
		print(printBoard(T))
		print("Draw")
		break
