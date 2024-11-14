from twttr import shorten

def test_twttr_upper():
    assert shorten("SHORT") == "SHRT"
    assert shorten("FKMYLF") == "FKMYLF"


def test_twttr_lower():
    assert shorten("suzan") == "szn"
    assert shorten("FRBRGF") == "FRBRGF"


def test_twttr_num():
    assert shorten("1830") == "1830"

def test_twttr_punc():
    assert shorten(">?()_+") == ">?()_+"

