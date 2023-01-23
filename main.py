from flask import flask

app = Flask(_name_)

@app.route("/")
def index():
  return "Congrats, it's a web app!"


from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0, 2)]

#set player to False
player = False

while player == False:
  #set player to True
  player = input("Rock", "Paper", "Scissors?")
  if player == computer:
    print("Tie!")
  elif player == "Rock":
    if computer == "Paper":
      print ("The machines win this round", player, "gets covered by", computer)
    else:
      print ("You win!", player, "decimates", computer)
  elif player == "Paper":
    if computer == "Scissors":
      print ("You lose, shame on you.", player, "is shredded by", computer)
    else:
      print ("Congrats! You win.", player, "covers", computer)
  elif player == "Scissors":
      if computer == "Rock":
        print ("You lose, shame on you.", player, "gets beaten down by", computer)
      else:
        print ("Congrats! You win.", player, "shreds", computer)
  else:
    print ("That is not a valid choice, please check your spelling!")
   
  player = False
  computer = t[randint(0,2)]

if _name_ == "_main_":
  app.run(host = "127.0.0.1", port = 8080, debug = True)
  
           
