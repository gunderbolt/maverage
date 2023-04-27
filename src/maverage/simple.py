"""Implements the Simple Moving Average."""
# For math behind the Simple Moving Average, refer to
# https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average

from collections import deque


class Simple:
    """Simple Moving Average"""
    def __init__(self, size) -> None:
        self._deque = deque([])
        self._cumulative = 0

        self._samples = 0
        self._size = size

    def input(self, value) -> None:
        """Input next value. Do not calculate the average yet."""
        if self._samples < self._size:
            self._cumulative += value
            self._samples += 1
            self._deque.appendleft(value)
        else:
            old_value = self._deque.pop()
            self._cumulative += value - old_value
            self._deque.appendleft(value)

    def calc_input(self, value) -> float:
        """Input the next value and return the calculated average."""
        self.input(value)
        return self.average

    @property
    def average(self) -> float:
        """Get the current average of the internal data."""
        return self._cumulative / self._samples


if __name__ == '__main__':
    sma = Simple(3)

    v = sma.calc_input(1)
    assert v==1
    assert v==sma.average

    v = sma.input(2)
    assert v==None
    assert sma.average==1.5

    v = sma.calc_input(3)
    assert v==2
    assert v==sma.average

    v = sma.input(4)
    assert v==None
    assert sma.average==3

    v = sma.calc_input(5)
    assert v==4
    assert v==sma.average

    print(sma)
    print(sma.average)
