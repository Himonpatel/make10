import pytest
from project import evaluate_expression, is_valid_expression, find_solution

def test_evaluate_expression():
    assert evaluate_expression("2+3+5") == 10
    assert evaluate_expression("10/2") == 5
    assert evaluate_expression("5/0") is None
    assert evaluate_expression("invalid") is None

def test_is_valid_expression():
    assert is_valid_expression("1+2+3+4", [1, 2, 3, 4]) == True
    assert is_valid_expression("1+2+(3+4)", [1, 2, 3, 4]) == True
    assert is_valid_expression("1+2+(3+4)+5", [1, 2, 3, 4]) == False  # Too many digits
    assert is_valid_expression("1+2+3+4", [4, 3, 2, 1]) == False       # Wrong order

def test_find_solution():
    # This is hard to test because it’s randomized, so test known values
    assert find_solution([2, 2, 3, 3]) in [
        "2+2+3+3", "2+(2+3)+3", "(2+2)+3+3",  # Accept variations that give 10
        "(2+2+3)+3", "2+(2+3+3)", "(2+2)+(3+3)"
    ]
