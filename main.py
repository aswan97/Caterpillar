from flask import flask
from flask import request
from random import randint

app = Flask(_name_)

@app.route("/")
def index():
  player = request.args.get("player", "")
  if player:
    result = r_p_s(player)
  else:
    result = ""
  return (
    """<form action="" method="get">
              <input type="text" name="player">
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

  """set player to False"""
  player = False

  while player == False:
    """set player to True"""
    player = input("Rock", "Paper", "Scissors?")
    if player == computer:
      result = print("Tie!")
    elif player == "Rock":
      if computer == "Paper":
        result = print ("The machines win this round", player, "gets covered by", computer)
      else:
        result = print ("You win!", player, "decimates", computer)
    elif player == "Paper":
      if computer == "Scissors":
        result = print ("You lose, shame on you.", player, "is shredded by", computer)
      else:
        result = print ("Congrats! You win.", player, "covers", computer)
    elif player == "Scissors":
      if computer == "Rock":
        result = print ("You lose, shame on you.", player, "gets beaten down by", computer)
      else:
        result = print ("Congrats! You win.", player, "shreds", computer)
    else:
  result = print ("That is not a valid choice, please check your spelling!")
  
  return str(result)
   
  """player = False
  computer = t[randint(0,2)]"""

if _name_ == "_main_":
  app.run(host = "127.0.0.1", port = 8080, debug = True)
  
           
