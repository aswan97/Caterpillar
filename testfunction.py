
# Online Python - IDE, Editor, Compiler, Interpreter

from random import randint

def r_p_s(player):
    """create a list of play options"""
    t = ["Rock", "Paper", "Scissors"]
    """assign a random play to the computer"""
    computer = t[randint(0, 2)]
    """player = input("Rock", "Paper", "Scissors?")"""
    if player == computer:
      return print("Tie!")
    elif player == "Rock":
      if computer == "Paper":
        return print ("The machines win this round", player, "gets covered by", computer,".")
      else:
        return print ("You win!", player, "decimates", computer,".")
    elif player == "Paper":
      if computer == "Scissors":
        return print ("You lose, shame on you.", player, "is shredded by", computer,".")
      else:
        return print ("Congrats! You win.", player, "covers", computer,".")
    elif player == "Scissors":
      if computer == "Rock":
        return print ("You lose, shame on you.", player, "gets beaten down by", computer,".")
      else:
        return print ("Congrats! You win.", player, "shreds", computer,".")
    else:
        return print ("That is not a valid choice, please check your spelling!")

play = input("Would you like to play Rock, Paper, Scissors?: ")
while play == "Yes":
    player = input("Please enter Rock, Paper, or Scissors: ")
    r_p_s(player)
    play = input("Would you like to play again? ")
else:
    print("We hope you change your mind!")
