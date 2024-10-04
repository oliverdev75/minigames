import random
from .resources.console import (
    info,
    success,
    warning,
    prompt_int
)

def main():
    rand_number = random.randint(1, 10)
    user_number = 0

    info("Game starts!")
    while user_number != rand_number:
        user_number = prompt_int("Guess the number (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        if user_number < rand_number:
            warning("You are lower than the number")
        elif user_number > rand_number:
            warning("You are higher than the number")

    success("Congrats!! You won.")