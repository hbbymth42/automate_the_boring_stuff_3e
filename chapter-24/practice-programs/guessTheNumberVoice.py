# This is a guess the number game.
import random, pyttsx3
secret_number = random.randint(1, 20)
pyttsx3.speak("I am thinking of a number between 1 and 20.")

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    pyttsx3.speak("Take a guess.")
    guess = int(input(">"))

    if guess < secret_number:
        pyttsx3.speak(f"You guess, {guess}, is too low.")
    elif guess > secret_number:
        pyttsx3.speak(f"Your guess, {guess}, is too high.")
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    pyttsx3.speak("Good job! You got it in " + str(guesses_taken) + " guesses!")
else:
    pyttsx3.speak("Nope. The number was " + str(secret_number))
