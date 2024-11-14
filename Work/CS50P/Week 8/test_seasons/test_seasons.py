import pytest
from seasons import get_delta_words

def test_get_delta_days():
    assert get_delta_words("1995-07-17") == "Fourteen million, nine hundred seventy-one thousand, six hundred eighty minutes"
    assert get_delta_words("1995-07-18") == "Fourteen million, nine hundred seventy thousand, two hundred forty minutes"
    assert get_delta_words("1992-12-12") == "Sixteen million, three hundred thirty-five thousand, three hundred sixty minutes"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_delta_words("July 17, 1995")
        get_delta_words("1995.07.17")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Invalid date"







