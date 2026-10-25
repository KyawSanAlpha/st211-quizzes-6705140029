import pytest

@pytest.mark.parametrize("value, expected", [
    pytest.param(2, 4, id="two_squared"),
    pytest.param(3, 9, id="three_squared"),
    pytest.param(4, 16, id="four_squared"),
])
def test_square(value, expected):
    assert value ** 2 == expected
    