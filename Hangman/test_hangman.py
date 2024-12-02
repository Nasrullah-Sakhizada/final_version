import pytest
from hangman import check_guess  # Assume you have a `check_guess` function

def test_correct_guess():
    assert check_guess('a', 'apple', ['_']) == (True, ['a', '_', '_', '_', '_'])

def test_wrong_guess():
    assert check_guess('z', 'apple', ['_']) == (False, ['_'])
