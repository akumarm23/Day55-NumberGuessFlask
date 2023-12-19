# Number Guessing Game using Flask in Python v0.1

from flask import Flask
import random

# Initialize Flask application
app = Flask(__name__)

# Generate a random number between 0 and 9 for the user to guess
number_to_guess = random.randint(0, 9)
print(number_to_guess)  # For testing purposes, remove in production

# Define the root route, providing instructions and an initial image
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

# Define a route that takes a user's guess as an integer parameter
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number_to_guess:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < number_to_guess:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# Run the application if executed as the main module
if __name__ == "__main__":
    app.run(debug=True)
