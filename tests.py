import pytest
from unittest.mock import patch
from io import StringIO

from mainCode import read_integer_between_numbers, read_nonempty_string
import builtins
from unittest.mock import patch

def test_read_integer_between_numbers_valid_input():
    with patch.object(builtins, 'input', side_effect=['5']):
        result = read_integer_between_numbers("Enter a number: ", 1, 10)
    assert result == 5

if __name__ == '__main__':
    pytest.main()
