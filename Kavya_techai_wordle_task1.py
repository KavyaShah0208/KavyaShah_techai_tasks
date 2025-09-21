import random

GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"

with open("five_letter_words.txt", "r") as f:
    word_list = [line.strip().lower() for line in f if line.strip()]

word = random.choice(word_list)
length = 5
lives = 6
print(word)
print("It is a", length, "letter word")
print("_ " * length)
print()
print("You have", lives, "chances to guess the word\n")

while lives > 0:
    guess = input("Enter your guess: ").lower()

    if len(guess) != length :
        print("Invalid input. Enter a valid", length, "letter word.\n")
        continue

    display = ""
    for i in range(length):
        if guess[i] == word[i]:
            display += GREEN + guess[i].upper() + RESET
        elif guess[i] in word:
            display += YELLOW + guess[i].upper() + RESET
        else:
            display += GRAY + guess[i].upper() + RESET

    print(display + "\n")

    if guess == word:
        print(GREEN + "Word Guessed: " + word.upper() + RESET)
        break

    lives -= 1
    print("Lives left:", lives, "\n")

if lives == 0 and guess != word:
    print(GRAY + "Out of lives! The word was: " + word.upper() + RESET)
