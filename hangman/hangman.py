import os
import random
from .resources.console import (
    prompt,
    info,
    warning,
    success
)


def get_word() -> str:
    words = []
    with open(f"{os.getcwd()}/hangman/words.txt") as file:
        for word in file:
            words.append(word.strip())

    return words[random.randint(0, 29)]

def check_letter(letter, word, incomplete_word):
    index = -2
    count = 0
    
    while index != -1:
        if index == -2:
            index = -1

        index = word.find(letter, index + 1)
        if index != -1:
            incomplete_word[index] = letter
            count = count + 1
    if count > 0:
        return incomplete_word
    else:
        return False
        


def main():
    word = get_word()
    incomplete_word = [char for char in ('_'*len(word))]
    lifes = len(word) * 2
    letter = ""
    allowed_letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    
    info("Game starts!!")
    while '_' in incomplete_word and lifes > 0:
        print(f"Lifes: {lifes}")
        print(f"Word: {''.join(incomplete_word)}")
        letter = prompt("Introduce a letter: ", allowed_letters)

        if check_letter(letter, word, incomplete_word):
            if '_' in incomplete_word:
                success("Nice! You guessed a letter.")
        else:
            lifes = lifes - 1
            if lifes > 0:
                warning("Ouups! You lost a life.")
    
    if lifes > 0:
        success("Well done! You won.")
        print(f"The word was: {word}")
    else:
        print("\nWhat a shame! You lost.")
        print(f"The word was: {word}")


