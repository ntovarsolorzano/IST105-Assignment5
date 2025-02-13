#!/usr/bin/env python3

import cgi
import cgitb
import math
import random
import sys
import os
from urllib.parse import urlencode

cgitb.enable()

def number_puzzle(number):
    """Checks if a number is even or odd and performs calculations."""
    try:
        number = int(number)
        if number % 2 == 0:
            result = f"The number {number} is even. Its square root is {math.sqrt(number)}"
        else:
            result = f"The number {number} is odd. Its cube is {number ** 3}"
        return result
    except ValueError:
        return "Invalid number. Please enter a valid integer."

def text_puzzle(text):
    """Converts text to binary and counts vowels."""
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    return binary_text, vowel_count

def treasure_hunt():
    """Simulates a treasure hunt guessing game."""
    secret_number = random.randint(1, 100)
    guesses_left = 5
    guessed_correctly = False

    while guesses_left > 0:
        #Simulate user guessing
        guess = random.randint(1,100)
        if guess == secret_number:
            guessed_correctly = True
            break
        guesses_left -= 1

    if guessed_correctly:
        return "Congratulations! You found the treasure!"
    else:
        return f"Sorry, you ran out of guesses. The number was {secret_number}."

# Main execution block
if __name__ == "__main__":
    form = cgi.FieldStorage()
    number = form.getvalue("number")
    text = form.getvalue("text")

    number_result = number_puzzle(number)
    text_binary, vowel_count = text_puzzle(text)
    treasure_result = treasure_hunt()

    # Prepare the URL with the results
    query_string = urlencode({
        "number_result": number_result,
        "text_binary": text_binary,
        "vowel_count": vowel_count,
        "treasure_result": treasure_result
    })

    # Redirect back to the PHP page with the results in the URL
    print("Content-Type: text/html") # HTTP header
    print() # Blank line to separate headers from content
    print(f"<meta http-equiv='refresh' content='0;url=form.php?{query_string}'>")
    print("<p>Redirecting...</p>")  # Optional message while redirecting
