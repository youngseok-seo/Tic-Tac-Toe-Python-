import random

def genBoard():

   #create the behind-the-scenes board

   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   
   #check for errors

   if len(T) != 9:
      return False

   for val in T:
      if (val != 0) and (val != 1) and (val != 2):
         return False

   #create board shown to user

   board = [0,1,2,3,4,5,6,7,8]
   
   #insert "X" or "O" into user-assigned slot

   for i in range (0,len(T),1):
      if T[i] == 0:
         board[i] = i
      elif T[i] == 1:
         board[i] = "X"
      elif T[i] == 2:
         board[i] = "O"
   
   #print new board

   line = "---|---|---"
   space = " | "
   
   print(" " + str(board[0]) + space + str(board[1]) + space + str(board[2]) + " ")
   print(line)
   print(" " + str(board[3]) + space + str(board[4]) + space + str(board[5]) + " ")
   print(line)
   print(" " + str(board[6]) + space + str(board[7]) + space + str(board[8]) + " ")
   
   return True

def analyzeBoard(T):

   #return 0 for In-play
   #return 1 for "X" wins 
   #return 2 for "O" wins
   #return 3 for Draw
   #return -1 for ERROR

   #check for errors

   for val in T:
      if (val != 0) and (val != 1) and (val != 2):
         return -1

   #analyze rows

   for i in range(0,7,3):
      row = T[i] * T[i+1] * T[i+2]
      if row == 1:
         return 1
      elif row == 8:
         return 2

   #analyze columns

   for i in range(0,3,1):
      col = T[i] * T[i+3] * T[i+6]
      if col == 1:
         return 1
      elif col == 8:
         return 2

   #analyze diagonals

   diag1 = T[0] * T[4] * T[8]
   diag2 = T[2] * T[4] * T[6]
   if (diag1 == 1) or (diag2 == 1):
      return 1
   elif (diag1 == 8) or (diag2 == 8):
      return 2

   #check if the game is In-play

   for val in T:
      if val == 0:
         return 0

   #if the above conditions are not met, the game is a Draw

   return 3

def opponent(player):
   if player == 1:
      return 2
   if player == 2:
      return 1

def genWinningMove(T,player):
   
   #generate an offensive move that will win the game
   #return -1 for ERROR

   for i in range(0,9,1):
      copyT = list(T)
      if copyT[i] == 0:
         copyT[i] = player
         if analyzeBoard(copyT) == player:
            return i

   return -1

def genNonLosingMove(T,player):
   
   #generate a defensive move that will prevent the opponent from winning

   return genWinningMove(T,opponent(player))

def genOpenMove(T):

   #generate the first open slot
   #return -1 for ERROR

   for i in range(0,9,1):
      if T[i] == 0:
         return i

   return -1

def genRandomMove(T):

   #check if there is an empty slot
   #return -1 for ERROR

   empty = False
   for val in T:
      if val == 0:
         empty = True
         break

   if empty == False:
      return -1

   #generate a random move
   #use recursion if necessary
   
   randmove = random.randint(0,8)
   if T[randmove] == 0:
      return randmove
   else:
      return genRandomMove(T)

