#modules - library which has 1 or more func shared with others
#import - a way to load modules into your codespace
#from random import choice
import random
"""
coin = random.choice(["heads", "tails"])
print(coin)

#from - loads the function to the local namespace, no need to specify
#'nameofmodule.function()', only 'function()'

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""
"""
import statistics

print(statistics.mean([100, 90]))
"""
"""
import sys

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#package - a third party library also available to everyone

import cowsay

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
"""


