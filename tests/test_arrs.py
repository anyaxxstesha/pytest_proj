from utils import arrs
from utils import dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], None, 3) == [1, 2, 3]


def test_get_val():
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 2, 'git') == 'two'
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 4, 'git') == 'git'
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 4, 'another') == 'another'
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 2, None) == 'two'
