
HANGMAN GAME
implemented in Python! 

About the Game:
- Guess letters to uncover the hidden word.
- You have "10 lives" to guess the word correctly.
- Each wrong guess costs a life.
- The game ends when:
  *You guess the word correctly (YOU WIN ).
  *You lose all your lives (GAME OVER ).

Features:
- Fun ASCII art for each stage of the game.
- Tracks guessed letters to avoid repeated inputs.
- Clear and user-friendly interface.
- Handles edge cases like invalid inputs or repeated guesses.
Dockerization:
- How to Build the Docker Image:
'''bash
---docker build -t hangman-game .
-How to Run the Docker Container:
'''bash:
---docker run --rm -it hangman-game

 Unit and Integration Tests:
How to run the test:
- Install pytest:
  ```bash
 --- pip install pytest
 ---pytest


