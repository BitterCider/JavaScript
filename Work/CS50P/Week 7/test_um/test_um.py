from um import count

def test_um_punct():
    assert count("hello, um, world") == 1
    assert count("um thanks... um") == 2
    assert count("..um... hi") == 1

def test_um_in_words():
    assert count("yummy") == 0
    assert count("album of the year") == 0
    assert count("umbrella") == 0
def test_um_case():
    assert count("Um LOL") == 1
    assert count("um.. UM..") == 2
