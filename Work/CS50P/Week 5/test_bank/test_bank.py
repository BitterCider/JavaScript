from bank import value

def test_bank_case():
    assert value("ho ho ho") == 20
    assert value("Ho Ho Ho") == 20
    assert value("sup newman") == 100
    assert value("SUP NEWMAN") == 100
    assert value("Hello") == 0
    assert value("hello") == 0

def test_bank_num_punc():
    assert value("Hello there #4") == 0
    assert value("How you doin'?") == 20
    assert value("I HAVE HOW MUCH IN MY ACCOUNT?!") == 100
    assert value("2 dollars and 5 cents sir") == 100
    assert value("...'Cause 7 8 9 LOL!") == 100







