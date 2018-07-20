import pytest

from src import code

@pytest.mark.parametrize(
    'num,result',
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24)
    ]
)
def test_factorial(num, result):
    assert code.factorial(num) == result


@pytest.mark.parametrize(
    'num,result',
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5)
    ]
)
def test_fibonacci(num, result):
    assert code.fibonacci(num) == result
