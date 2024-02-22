import json
import random

def load_words_from_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data["words"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    # Load words from a JSON file (replace "words.json" with your actual file path)
    word_list = load_words_from_json("words.json")

    # Choose a random word from the list
    word_to_guess = choose_word(word_list)
    guessed_letters = set()
    max_attempts = 6

    print("Welcome to Hangman!")
    while max_attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            max_attempts -= 1
            print(f"Incorrect guess. {max_attempts} attempts remaining.")

    if max_attempts == 0:
        print(f"Sorry, you're out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    main()
