# test_main.py

from main import caller

def test_pass():
    """
    This test should pass because 2 + 3 = 5.
    """
    assert caller('+', 2, 3) == 5

def test_fail():
    """
    This test will deliberately fail because division by should not be possible
    """
    caller('/', 2, 0)
    assert caller('+', '2', '3') == '5'
