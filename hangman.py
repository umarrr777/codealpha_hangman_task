import random

def hangman():
    words = ['python', 'programming', 'chatbot', 'hangman', 'developer', 'software']
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts}")

        # Show current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

        if "_" not in display_word:
            print("\nCongratulations! You won!")
            break
    else:
        print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
