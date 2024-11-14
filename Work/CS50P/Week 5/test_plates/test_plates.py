from plates import is_valid

def test_plates_num():
    assert is_valid("12") == False
    assert is_valid("12DAKO") == False
    assert is_valid("DH25KO") == False
    assert is_valid("A2") == False
    assert is_valid("DAK120") == True
    assert is_valid("DAK021") == False
    assert is_valid("KUSKUS") == True

def test_plates_punc():
    assert is_valid("PO_@12") == False
    assert is_valid("8IGA$$") == False

def test_plates_len():
    assert is_valid("AA") == True
    assert is_valid("") == False
    assert is_valid("A") == False



