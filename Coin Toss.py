import CoinClass as c
#not importing name of class but name of file
#name of class is coin
#taking whole file and putting all that code on the top
#alias as c to make it easier

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
#everytime you want a new instance you do the same c.Coin()
       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())
#once you create the instance, the instance is what you use to access the methods and stuff
           


       

# Call the main function.

main()
