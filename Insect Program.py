import InsectClass as c


def main():
    my_flight = c.Insect()

    my_flight.flight()
    
    print("The number of miles is:", my_flight.get_flight())


main()