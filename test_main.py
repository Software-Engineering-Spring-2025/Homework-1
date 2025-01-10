# test_main.py

from main import add_numbers

def test_add_numbers_pass():
    """
    This test should pass because 2 + 3 = 5.
    """
    assert add_numbers(2, 3) == 5

def test_add_numbers_fail():
    """
    This test will deliberately fail because 2 + 2 ≠ 5.
    """
    assert add_numbers(2, 2) == 5
