import os
import pytest

from lib.utils.decorators import requires_presence_of_file
from lib.exceptions.FileNotFound import FileNotFoundException

def test_requires_presence_of_file():
    def mock_func(num):
        return num

    # Verify that the function works fine without the decorator.
    without_decorator_value = mock_func
    assert without_decorator_value(1) == 1

    # Verify that an error is raised when the decorator is applied and file is not present.
    with_decorator = requires_presence_of_file('test.yml')(mock_func)
    with pytest.raises(FileNotFoundException):
        with_decorator(1)

    # Verify that no error is raised when decorator is applied and file is present.
    file = open('test.yml', 'w')
    with_correct_file_and_decorator = requires_presence_of_file('test.yml')(mock_func)

    try:
        with_correct_file_and_decorator_val = with_correct_file_and_decorator(1)

        assert with_correct_file_and_decorator_val == 1
    finally:
        os.remove('test.yml')
