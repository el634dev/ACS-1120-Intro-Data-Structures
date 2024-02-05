"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import txt_file
from sample import histogram_builder, random_words

app = Flask(__name__)

# Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    generate_histogram = histogram_builder(txt_file)

    return random_words(generate_histogram)

# -----------------------
# Favorites route
@app.route("/favorites")
def hello_world():
    """Return hello world"""
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.3.x/server/#in-code"""
    app.run(debug=False)
