import random

def choose_word():
    words = ["python", "hangman", "developer", "internship", "challenge", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while max_attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print("Incorrect! Attempts remaining:", max_attempts)
            print_hangman(max_attempts)

        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if max_attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

def print_hangman(attempts_left):
    hangman_graphics = [
        """
         -----
         |   |
             |
             |
             |
             |
        """
        ,
        """
         -----
         |   |
         O   |
             |
             |
             |
        """
        ,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        """
        ,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        """
        ,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        """
        ,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        """
        ,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        """
    ]

    print(hangman_graphics[6 - attempts_left])

if __name__ == "__main__":
    hangman()
