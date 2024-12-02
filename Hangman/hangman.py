import random
from hangman_art import stages, logo


word_list: list[str] = ["code", "academy", "lesson", "beginner", "python", "hangman"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 10.
lives: int = 10

chosen_word: str = random.choice(word_list)
print(logo)
print("Welcome to Hangman!")



placeholder: str = ""
word_length: int = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)



game_over: bool = False
correct_letters: list[str] = []

while not game_over:
    print(f"****************************{lives}/10 LIVES LEFT****************************")
    guess: str = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
    

    if guess in correct_letters:
        print(f"You've already guessed {guess}. Try again.")
       
    
    display: str = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display) 

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print(print(f"😞😞😞 IT WAS {chosen_word}! YOU LOSE 😞😞😞"))
            exit()
    if "_" not in display:
        game_over = True
        print(f"😊😊😊 IT WAS {chosen_word}! YOU WIN 😊😊😊")  
        exit()
    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.

    print(stages[10 - lives])