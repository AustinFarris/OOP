import random

# The Coin class simulates a coin that can
# be flipped.
# use upper case to separate variables from functions

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
# self always the first parameter we need
#creating attribute called sideup and setting it to heads
#method is called a mutator method, can change the value of an attribute, also called a set method
#set method is a mutator method that allow syou to change the value of an attribute
#Get method just returns the value of an attribute, accessor method
#mutator changes, accessor returns
#want to separate differnt method
#only do one thing in a method

    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
#changes, mutator
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
#returns, accessor
    def get_sideup(self):
            return self.sideup
