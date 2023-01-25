from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
  celsius = request.args.get("celsius", "")
  month = request.args.get("month", "")
  if celsius and month:
    fahrenheit = fahrenheit_from(celsius)
    name_of_month = get_month(month)
    advice = is_it_warm(fahrenheit)
  else:
    fahrenheit = ""
    name_of_month = ""
    advice = ""
  return (
    """<form action= "" method="get">
          <h1> Hope you are having a great day! </h1>
          Celsius Temperature: <input type="text" name="celsius"><br></br>
          Please enter the month in number form (1:12): <input type="text" name="month"><br></br>
          <input type="submit" value="Submit">
        </form> """
      + "The temperature is "
      + fahrenheit 
      + " F "
      + " in the month of "
      + name_of_month
      + "!"
      + "<br></br>"
      + advice
  )

def fahrenheit_from(celsius):
  """Convert Celsius to Fahrenheit"""
  try:
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)
    return str(fahrenheit)
  except ValueError:
    return "Invalid Input"

def get_month(month):
  """Translate the Number of the Month to the Actual Month"""
  try:
    month = int(month)
    if month == 1:
      name_of_month = "January"
      return name_of_month
    elif month == 2:
      name_of_month = "February"
      return name_of_month
    elif month == 3:
      name_of_month = "March"
      return name_of_month
    elif month == 4:
      name_of_month = "April"
      return name_of_month
    elif month == 5:
      name_of_month = "May"
      return name_of_month
    elif month == 6:
      name_of_month = "June"
      return name_of_month
    elif month == 7:
      name_of_month = "July"
      return name_of_month
    elif month == 8:
      name_of_month = "August"
      return name_of_month
    elif month == 9:
      name_of_month = "September"
      return name_of_month
    elif month == 10:
      name_of_month = "October"
      return name_of_month
    elif month == 11:
      name_of_month = "November"
      return name_of_month
    elif month == 12:
      name_of_month = "December"
      return name_of_month 
    else:
      return "That is not one of the 12 months!"
  except ValueError:
    return "Invalid Input"

def is_it_warm(fahrenheit):
  fahrenheit = float(fahrenheit)
  if fahrenheit > 50.0:
      advice = "It's decently warm out there, a coat is not needed!"
  else:
      advice = "Better bundle up!"
  return str(advice)

if __name__ == "__main__":
  app.run(host="127.0.0.1", port = 8080, debug = True)
