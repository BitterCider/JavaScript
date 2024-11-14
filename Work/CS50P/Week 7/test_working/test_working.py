from working import convert
import pytest

def test_convert_no_colon():
    assert convert("5 AM to 6 AM") == "05:00 to 06:00"
    with pytest.raises(ValueError):
        convert("2 PM - 5 AM")
    with pytest.raises(ValueError):
        convert("0 PM to 9 AM")
    with pytest.raises(ValueError):
        convert("5AM to 6PM")
    with pytest.raises(ValueError):
        convert("13 PM to 15 PM")

def test_convert_colon():
    assert convert("6:00 AM to 8:00 AM") == "06:00 to 08:00"
    with pytest.raises(ValueError):
        convert("8:60 PM to 5:65 AM")
    with pytest.raises(ValueError):
        convert("9:0 PM to 5:1 AM")
    with pytest.raises(ValueError):
        convert("6:00 AM - 8:00 AM")
    with pytest.raises(ValueError):
        convert("6:00AM to 8:00PM")
    





