import math

import pytest

from triangle.eq import eq_t


def test_ea_fail():
    a = 3
    area = eq_t(a)
    assert area == pytest.approx(9 * math.sqrt(3) / 4)


def test_ea_pass():
    a = 1
    area = eq_t(a)
    assert area == pytest.approx(math.sqrt(3) / 4)