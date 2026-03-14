import pytest
from src.decorators import my_function1


def test_log(capsys):

    my_function1(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function1 ok\n"


def test_log2(capsys):
    my_function1(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function1 error: ZeroDivisionError. Inputs: (4, 0), {}\n"


def test_log3(capsys):
    my_function1(
        4,
    )
    captured = capsys.readouterr()
    assert captured.out == "my_function1 error: TypeError. Inputs: (4,), {}\n"
