import os
import pytest

from lib.utils.decorators import requires_presence_of_file, with_additional_kwargs, requires_presence_of_dir
from lib.exceptions.FileNotFound import FileNotFoundException
from lib.exceptions.DirNotFound import DirNotFoundException

def test_requires_presence_of_file():
    '''
    This decorator should raise FileNotFoundException if the wrapped function
    attemps to execute when this file is not present. Otherwise, it should continue
    normally.
    '''
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


def test_with_additional_kwargs():
    '''
    This decorator injects additional kwargs into the kwargs list that the function
    was originally called with. We assert that the new kwargs are defined and the length
    of the dict increases.
    '''
    def with_length(**kwargs):
        kwargs.update({
            'len': len(kwargs)
        })
        return kwargs

    without_decorator_val = with_length(a=1, b=2)
    with_decorator = with_additional_kwargs(c=3, d=4)(with_length)
    with_decorator_val = with_decorator(a=1, b=2)

    assert with_decorator_val['len'] == without_decorator_val['len'] + 2
    assert with_decorator_val['a'] == 1
    assert with_decorator_val['b'] == 2
    assert with_decorator_val['c'] == 3
    assert with_decorator_val['d'] == 4

def test_requires_presence_of_dir():
    '''
    This decorator should raise DirFoundException if the wrapped function
    attemps to execute when the directory is not present. Otherwise, it should continue
    normally.
    '''
    def mock_func(num):
        return num

    # Verify that the function works fine without the decorator.
    without_decorator_value = mock_func
    assert without_decorator_value(1) == 1

    # Verify that an error is raised when the decorator is applied and file is not present.
    with_decorator = requires_presence_of_dir(os.getcwd() + 'test_dir')(mock_func)
    with pytest.raises(DirNotFoundException):
        with_decorator(1)

    # Verify that no error is raised when decorator is applied and file is present.
    os.makedirs(os.getcwd() + 'test_dir')
    with_correct_file_and_decorator = requires_presence_of_dir('test_dir')(mock_func)

    try:
        with_correct_file_and_decorator_val = with_correct_file_and_decorator(1)

        assert with_correct_file_and_decorator_val == 1
    finally:
        os.rmdir(os.getcwd() + 'test_dir')

