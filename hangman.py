import random
from hangman_art import stages, logo

word_list: list[str] = ["code", "academy", "lesson", "beginner", "python", "hangman"]

def choose_word(words: list[str]) -> str:
    return random.choice(words)

def initialize_placeholder(word: str) -> str:
    return "_" * len(word)

def update_display(word: str, correct_letters: list[str]) -> str:
    return "".join(letter if letter in correct_letters else "_" for letter in word)

def process_guess(guess: str, word: str, correct_letters: list[str], lives: int) -> tuple[int, bool]:
    if guess in word:
        if guess not in correct_letters:
            correct_letters.append(guess)
        return lives, True
    else:
        return lives - 1, False

def display_state(word: str, correct_letters: list[str], lives: int):
    print(f"Word to guess: {update_display(word, correct_letters)}")
    print(f"****************************{lives}/10 LIVES LEFT****************************")
    print(stages[10 - lives])

def main():
    print(logo)
    print("Welcome to Hangman!")
    
    chosen_word = choose_word(word_list)
    lives = 10
    correct_letters = []
    placeholder = initialize_placeholder(chosen_word)

    game_over = False
    while not game_over:
        display_state(chosen_word, correct_letters, lives)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in correct_letters:
            print(f"You've already guessed {guess}. Try again.")
            continue

        lives, correct = process_guess(guess, chosen_word, correct_letters, lives)

        if not correct:
            print(f"You guessed {guess}, that's not in the word. You lose a life. Lives remaining: {lives}")

        if lives == 0:
            game_over = True
            print(f"😞😞😞 IT WAS {chosen_word}! YOU LOSE 😞😞😞")
        elif "_" not in update_display(chosen_word, correct_letters):
            game_over = True
            print(f"😊😊😊 IT WAS {chosen_word}! YOU WIN 😊😊😊")

if __name__ == "__main__":
    main()
