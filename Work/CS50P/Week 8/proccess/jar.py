class Jar:
    def __init__(self, capacity=12):
            #2 intializes respective setters
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        #7 calls getter of size
        #9 hands print the number of cookies, as per size
        return self.size*'🍪'


    def deposit(self, n):
        if n >= 0:
            #4 calls respective setter
            self.size += n
        else:
            raise ValueError("n must be non-negative")

    def withdraw(self, n):
        if n >= 0:
            #4 calls respective setter
            self.size -= n
        else:
            raise ValueError("n must be non-negative")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        #8 returns current value of size
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Too many cookies")
        if size < 0:
            raise ValueError("Not enough cookies")
            #5 if size valid, assigns it a new value per given n
        self._size = size

"""
1. jar instance is created
2. __init__ method is called within class Jar
3. self.capacity and self.size call their respective setters
4. setters assign _ value to self.size and self.capacity
5. jar.deposit and jar.withdraw call their respective methods
6. deposit(n) and withdraw(n) change the value of size based on given n
7. self.size within these methods calls the setter method and assigns size to self._size
8. print(jar) calls __str__ in which self.size calls the getter @property method
9. self._size is returned and printed
"""


#1 calls __init__
jar = Jar()

#3 calls deposit and withdraw methods
jar.capacity = 200 #(optional) calls @capacity.setter and changes its value
jar.deposit(10)
jar.withdraw(9)

#6 calls __str__ method
print(jar)

#10 number of cookies is printed
