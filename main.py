import random

print("Welcome to my Number Guessing Game! \n You will get 5 attempts to guess the number between 50 to 100.")

number_to_guess = random.randrange(50, 100)

chances = 5

guess_counter = 0  

while guess_counter < chances:
    guess_counter += 1
    your_guess = int(input("Please Enter your Guess Number: "))

    if your_guess == number_to_guess:
        print(
            f"Congratulations! The number is {number_to_guess} and you guessed it right in {guess_counter} attempts."
        )
        break  # The correct guess, so exit the loop

    elif guess_counter >= chances and your_guess != number_to_guess:
        print(f"Oops! Sorry, you guessed the wrong number. The number was {number_to_guess}. Better luck next time!")
        break  # Exit the loop after using all attempts

    elif your_guess < number_to_guess:
        print("Your guess is too low, try again!")

    elif your_guess > number_to_guess:
        print("Your guess is too high, try again!")
