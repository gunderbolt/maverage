'''Tests for the `Simple` moving average class.'''
import pytest

from maverage import Simple


@pytest.fixture()
def sma():
    """Create the Simple object sma to be used in tests."""
    simple = Simple(3)
    return simple


@pytest.mark.parametrize('test_input', [0, -1, 'string', 1.5, 2.0, None])
def test_invalid_size_argument(test_input):
    """Tests the __init__ method with invalid size arguments."""
    with pytest.raises(ValueError):
        Simple(test_input)


def test_moving_average(sma):  # pylint: disable=redefined-outer-name
    """Input values and check the results."""
    val = sma.calc_input(1)
    assert val==1

    val = sma.input(2)
    assert val is None
    assert sma.average==1.5

    val = sma.calc_input(3)
    assert val==2

    val = sma.input(4)
    # Do not check sma.average this time to show it is not necessary.

    val = sma.calc_input(5)
    assert val==4
