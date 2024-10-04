import random
from time import sleep
from .resources.console import (
    prompt_int,
    info,
    warning,
    success
)

ROCK = 1
PAPER = 2
SCISSORS = 3

def choose_element() -> int:
    print(f"Rock: {ROCK} Paper: {PAPER} Scissors: {SCISSORS}")
    return prompt_int("Choose: ", [1, 2, 3])


first_move = lambda player1, player2: player1 == ROCK and player2 == SCISSORS
second_move = lambda player1, player2: player1 == SCISSORS and player2 == PAPER
third_move = lambda player1, player2: player1 == PAPER and player2 == ROCK

def main():
    snake_points = 0
    user_points = 0
    snake_choice = 0
    user_choice = 0
    
    info("Game starts!")
    while user_points < 3 and snake_points < 3:
        snake_choice = random.randint(1, 3)
        print(f"User points: {user_points}, Snake points: {snake_points}")
        user_choice = choose_element()
        
        if (first_move(user_choice, snake_choice)
            or second_move(user_choice, snake_choice)
            or third_move(user_choice, snake_choice)):
            
            user_points += 1
            if user_points < 3 and snake_points < 3:
                success("Nice! You won 1 point.")

        elif (first_move(snake_choice, user_choice)
            or second_move(snake_choice, user_choice)
            or third_move(snake_choice, user_choice)):

            snake_points += 1
            if user_points < 3 and snake_points < 3:
                warning("Ouups! you lost")
        
        else:
            info("Oh! There's a tie.")
    
    if user_points == 3:
        success("Congratulations! You won.")
    else:
        print("Ohh! You lost.")