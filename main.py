from flask import flask
from flask import request
from random import randint

app = Flask(_name_)

@app.route("/")
def index():
  play = request.args.get("play", "")
  if play == "Yes":
    player = request.args.get("player", "")
    while play == "Yes":
      r_p_s(player)
      play = request.args.get("play", "")
    else:
      print("We hope you change your mind!")
  else:
    result = ""
  return (
    """<form action="" method="get">
              <input type="text" name="play">
              <input type="submit" value="Convert">
              </form>"""
      + play
  )
  return (
    """<form action="" method="get">
              <input type="text" name="play">
              <input type="submit" value="Convert">
              </form>"""
      + result
  )
    
@app.route("/<str:player>")
def r_p_s(player):
    """create a list of play options"""
    t = ["Rock", "Paper", "Scissors"]
    """assign a random play to the computer"""
    computer = t[randint(0, 2)]
    """player = input("Rock", "Paper", "Scissors?")"""
    if player == computer:
      result = print("Tie!")
      return result
    elif player == "Rock":
      if computer == "Paper":
        result = print ("The machines win this round", player, "gets covered by", computer,".")
        return result
      else:
        result = print ("You win!", player, "decimates", computer,".")
        return result
    elif player == "Paper":
      if computer == "Scissors":
        result = print ("You lose, shame on you.", player, "is shredded by", computer,".")
        return result
      else:
        result =  print ("Congrats! You win.", player, "covers", computer,".")
        return result
    elif player == "Scissors":
      if computer == "Rock":
        result = print ("You lose, shame on you.", player, "gets beaten down by", computer,".")
        return result
      else:
        result = print ("Congrats! You win.", player, "shreds", computer,".")
        return result
    else:
        result = print ("That is not a valid choice, please check your spelling!")
        return result

#play = input("Would you like to play Rock, Paper, Scissors?: ")
#while play == "Yes":
    #player = input("Please enter Rock, Paper, or Scissors: ")
    #r_p_s(player)
    #play = input("Would you like to play again? ")
#else:
    #print("We hope you change your mind!")


if _name_ == "_main_":
  app.run(host = "127.0.0.1", port = 8080, debug = True)
  
           
