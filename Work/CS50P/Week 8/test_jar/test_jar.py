from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_2 = Jar(5)
    assert jar_2.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) =="🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(2)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(9)

def test_withdraw():
    jar = Jar()
    jar.size = 10
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)




