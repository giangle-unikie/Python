import pytest
from insert_spaces import inserting_spaces

def test_inserting_spaces_no_capital_letters():
    input_string = "this is a test"
    expected_output = "this is a test"
    assert inserting_spaces(input_string) == expected_output

def test_inserting_spaces_one_word():
    input_string = "Test"
    expected_output = "Test"
    assert inserting_spaces(input_string) == expected_output

def test_inserting_spaces_multiple_words():
    input_string = "ThisIsAStringWithMultipleWords"
    expected_output = "This Is A String With Multiple Words"
    assert inserting_spaces(input_string) == expected_output

def test_inserting_spaces_empty_input():
    with pytest.raises(SystemExit):
        inserting_spaces("")

def test_inserting_spaces_special_characters():
    input_string = "ThisIs*ATest!"
    expected_output = "This Is* A Test!"
    assert inserting_spaces(input_string) == expected_output

