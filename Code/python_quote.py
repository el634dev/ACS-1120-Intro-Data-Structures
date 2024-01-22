"""Importing random lib to access randint"""
import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    """
    Desc: Generate a random quote/sentence
    Params: None
    Return: A random sentence generated from a random index
    """
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

# ---------------------------
# Able to import random_python_quote() and print a random sentence
if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
