from flask import flask

app = Flask(_name_)

@app.route("/")
def index():
  return "Congrats, it's a web app!"

if _name_ == "_main_":
  app.run(host = "127.0.0.1", port = 8080, debug = True)
  
           
