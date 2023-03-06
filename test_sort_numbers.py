import sys
from typing import List
import pytest
from sort_numbers import sorting_numbers

def test_sorting_numbers_only_integers():
    input_list = [1, 3, 2, 5]
    expected_output = [1, 2, 3, 5]
    assert sorting_numbers(input_list) == expected_output

def test_sorting_numbers_only_floats():
    input_list = [3.5, 1.0, 2.5, 0.5]
    expected_output = [0.5, 1.0, 2.5, 3.5]
    assert sorting_numbers(input_list) == expected_output

def test_sorting_numbers_mixed():
    input_list = [1, 3.5, 2.0, 0.5]
    expected_output = [0.5, 1, 2.0, 3.5]
    assert sorting_numbers(input_list) == expected_output

def test_sorting_numbers_invalid_input():
    with pytest.raises(SystemExit):
        sorting_numbers([2, "invalid", 1, 0.5])

def test_sorting_numbers_empty_list():
    input_list = []
    expected_output = []
    assert sorting_numbers(input_list) == expected_output