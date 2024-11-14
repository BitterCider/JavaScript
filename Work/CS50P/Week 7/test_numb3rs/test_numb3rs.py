from numb3rs import validate

def test_validate_range():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("25.25.25.1") == True
    assert validate("256.255.255.255") == False
    assert validate("2555.255.2.65") == False
    assert validate("255.256.256.256") == False

def test_validate_punc():
    assert validate("?!@.25..6.5") == False
    assert validate(">.!.^.%") == False
    assert validate(" . . . ") == False
    assert validate("9.2..4.5") == False


