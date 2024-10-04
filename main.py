#!/bin/env python3

from resources.console import (
    info,
    error,
    prompt
)
from guess_number import guess_number
from rock_paper_scissors import rock_paper_scissors
from hangman import hangman

def banner():
    print("""
        List of games:
            1.Guess the number
            2.Rock, paper, and scissors
            3.Hangman
        
          Press Enter to exit
    """)

def init():
    leave = False
    answer = 0

    print("""
        Welcome to Minigames, a place where you can play
        games like; guess the number and rock, paper, and scissors
    """)

    while not leave:
        banner()
        answer = input("Choose one: ")
        match answer:
            case '1':
                guess_number.main()
            case '2':
                rock_paper_scissors.main()
            case '3':
                hangman.main()
            case '':
                leave = True
                info("Good bye!")
            case _:
                error(f"Oups! The option {answer} does not exist. Use list numbers.")




if __name__ == '__main__':
    init()