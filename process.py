#!/usr/bin/env python3
import sys
import math
import random

# --- Function Definitions ---

def number_puzzle(num):
    """Processes the number puzzle."""
    if num % 2 == 0:  # Even
        return f"The number is even.  Square root: {math.sqrt(num):.2f}"
    else:  # Odd
        return f"The number is odd.  Cube: {num ** 3}"

def text_puzzle(text):
    """Processes the text puzzle."""
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
    return f"Binary: {binary_text}\nVowel Count: {vowel_count}"

def treasure_hunt():
    """Simulates the treasure hunt game."""
    secret_number = random.randint(1, 100)
    attempts = 0
    won = False
    guesses = []  # List to store the guesses

    while attempts < 5 and not won:
        attempts += 1
        guess = random.randint(1, 100)
        guesses.append(guess)  # Add the guess to the list

        if guess == secret_number:
            won = True

    if won:
        return f"You won the treasure in {attempts} attempts!\nGuesses: {', '.join(map(str, guesses))}" # Show guesses
    else:
        return f"You didn't find the treasure. The number was {secret_number}.\nGuesses: {', '.join(map(str, guesses))}" # Show guesses


# --- Main Script Logic ---

# Get arguments from the command line
if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    text = sys.argv[2]
except ValueError:
    print("Error: Invalid number input.")
    sys.exit(1)
except IndexError:
    print("Error: Missing arguments")
    sys.exit(1)

# Process the puzzles
number_result = number_puzzle(number)
text_result = text_puzzle(text)
treasure_result = treasure_hunt()

# Combine results and print
all_results = f"{number_result}\n\n{text_result}\n\n{treasure_result}"
print(all_results)