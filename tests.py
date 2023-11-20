import pytest
from unittest.mock import patch
from io import StringIO

from mainCode import read_integer_between_numbers, read_nonempty_string

def test_read_integer_between_numbers_valid_input():
    with patch('builtins.input', return_value='5'):
        result = read_integer_between_numbers("Enter a number between 1 and 10: ", 1, 10)
    assert result == 5

def test_read_integer_between_numbers_invalid_input_then_valid_input():
    with patch('builtins.input', side_effect=['abc', '5']):
        result = read_integer_between_numbers("Enter a number between 1 and 10: ", 1, 10)
    assert result == 5

def test_read_nonempty_string_valid_input():
    with patch('builtins.input', return_value='John'):
        result = read_nonempty_string("Enter a non-empty string: ")
    assert result == 'John'

def test_read_nonempty_string_empty_input_then_valid_input():
    with patch('builtins.input', side_effect=['', 'John']):
        result = read_nonempty_string("Enter a non-empty string: ")
    assert result == 'John'

# Add more tests for other functions...

if __name__ == '__main__':
    pytest.main()
