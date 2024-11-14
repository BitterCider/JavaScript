import pytest
from fuel import convert, gauge


def test_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("dog")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    assert convert("10/100") == 10
    assert convert("1/2") == 50
    assert convert("1/8") == 12

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(40) == "40%"





