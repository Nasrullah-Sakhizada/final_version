import unittest
from hangman import choose_word, initialize_placeholder, update_display, process_guess

def test_choose_word():
    words = ["code", "academy"]
    word = choose_word(words)
    assert word in words

def test_initialize_placeholder():
    word = "python"
    placeholder = initialize_placeholder(word)
    assert placeholder == "______"

def test_update_display():
    word = "python"
    correct_letters = ["p", "y"]
    display = update_display(word, correct_letters)
    assert display == "py____"

def test_process_guess_correct():
    word = "python"
    correct_letters = ["p"]
    lives = 10
    new_lives, correct = process_guess("y", word, correct_letters, lives)
    assert new_lives == 10
    assert correct
    assert "y" in correct_letters

def test_process_guess_incorrect():
    word = "python"
    correct_letters = ["p"]
    lives = 10
    new_lives, correct = process_guess("z", word, correct_letters, lives)
    assert new_lives == 9
    assert not correct
    assert "z" not in correct_letters
