#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sets a variable for the discounted ticket price.
DISCOUNT = .75

# Determines if a string could be a number or not.
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



# Make a function for a dotted line, for ease of reading.
def line():
    for i in range(100):
        print("-", end = "")

        
# The main function. It first asks for an appropriate destination then saves that as a global variable to be used throughout the program.       
def main():
    print("Potential Vacation Destinations\n")
    print("[1]:  Hawaii")
    print("[2]:  The Bahamas")
    print("[3]:  Cancun")
    print("[0]:  Exit the program")
    option_dest = input("\nPlease select an option by entering 1-3 or hit 0 to exit.\t")
    if isfloat(option_dest) == False:
        print("\nInvalid entry. Ending program.\n")
        return
    else:
        option_dest = int(option_dest)
        
    # Input verification for the destination using if-elif-else.
    while option_dest != 0:
        if option_dest == 1:
            dest = "Hawaii"
            break
        elif option_dest == 2:
            dest = "The Bahamas"
            break
        elif option_dest == 3:
            dest = "Cancun"
            break
        else:
            print("Invalid entry. Ending program.\n")
            option_dest = 0
            return
        
    # Sets global variable to be used outside of the function.
    if option_dest != 0:
        global destination
        destination = dest
        print("\nYou have selected ", dest, " as your destination.\n", sep = "")
        carrier()
    else:
        print("You've opted to exit. Ending program.\n")
        return               

    
# The next called function. It queries the user for an appropriate airline and airfare.
def carrier():
    print("\nPotential Airlines\n")
    print("[1]:  US Air")
    print("[2]:  Delta")
    print("[3]:  United")
    print("[0]:  Exit the program")
    option_carrier = input("\nPlease select an option by entering 1-3 or hit 0 to exit.\t")
    if isfloat(option_carrier) == False:
        print("\nInvalid entry. Ending program.\n")
        return
    else:
        option_carrier = int(option_carrier)
    while option_carrier != 0:
        if option_carrier == 1:
            carrier = "US Air"
            break
        else: 
            if option_carrier == 2:
                carrier = "Delta"
                break
            else: 
                if option_carrier == 3:
                    carrier = "United"
                    break
                else:
                    print("Invalid entry. Ending program.\n")
                    option_carrier = 0
                    return
                
    # sets a global variable for the airline to be used outside this function.            
    if option_carrier != 0:
        global airline
        airline = carrier
    else:
        print("You've opted to exit. Ending program.\n")
        return    
    
    # Query the user for what the want to pay in airfare.
    airfares = input("\nInput whatever roundtrip airfare you feel like paying that's greater than zero.\t")
    
   # Input verification for the airfare to ensure it's a number. 
    if isfloat(airfares) == False:
        print("\nInvalid entry. Ending program.\n")
        return
    else:
        airfares = int(airfares)
    
    # Input verification for the airfare to ensure its not less than or equal to zero. 
    if airfares <= 0:
        print("You have entered a value less than or equal to zero.")
        airfares = float(input("Input whatever roundtrip airfare you feel like paying that's greater than zero.\t"))
        
    # Sets a global variable for the airfare to be used outside the function.
    global airfare 
    airfare = airfares
    print("\nYou selected ", carrier, ".", sep = "")
    print("The round-trip airfare is ", "${:,.2f}".format(airfare), ".\n", sep = "")
    passenger()

    
# The next called function. It queries the user how many passengers are flying.    
def passenger():
    print("\nHow many total passengers are flying?")
    print("[1]:  One Passenger")
    print("[2]:  Two Passengers")
    print("[3]:  Three Passengers")
    print("[4]:  Four Passengers")
    print("[0]:  Exit the program")
    
    # Input verification for passenger selection.
    option_passengers = input("\nPlease select an option by entering 1-3 or hit 0 to exit.\t")
    if isfloat(option_passengers) == False:
        print("\nInvalid entry. Ending program.\n")
        return
    else:
        option_passengers = int(option_passengers)
    while option_passengers != 0:
        if option_passengers == 1:
            passenger = 1
            break
        elif option_passengers == 2:
            passenger = 2
            break
        elif option_passengers == 3:
            passenger = 3
            break
        elif option_passengers == 4:
            passenger = 4
            break
    if option_passengers == 0:
        print("Invalid entry. Ending program.\n")
        option_passengers = 0
        return

    # Query to determine how many of the passengers are under 18.
    minor = input("How many passengers are under 18? Minors receive a 25% discount.\t")
    if isfloat(minor) == False:
        print("\nInvalid entry. Ending program.\n")
        return
    else:
        minor = int(minor)
    
    # Input verification to ensure minors isn't greater than the total passengers or negative.
    if minor > passenger or minor < 0:
        print("\nYou have entered an incorrect value.")
        minor = int(input("How many passengers are under 18? Minors receive a 25% discount.\t"))
    
    # Converts local variables to global variables to be used outside the function.
    global minors
    minors = minor
    global adults
    adults = passenger - minor
    
    # Prints a confirmation of selections.
    if passenger == 1:
        print("\nYou have selected ", passenger, " total passenger.", sep = "")
    else:
        print("\nYou have selected ", passenger, " total passengers.", sep = "")
    if adults == 1:
        print("You have selected ", adults, " adult and", sep = "", end = " ")
    else:
        print("You have selected ", adults, " adults and", sep = "", end = " ")
    if minors == 1:
        print(minors, " minor.\n", sep = "")
    else:
        print(minors, " minors.\n", sep = "")
    
    calculation()
    
    
    

# Next function; this calculates the airfare based on the selections made and prints a summary of that information.
def calculation():
    print("Here is a summary of what you have chosen:\n")
    line()
    
    # Prints destination and airline.
    print("\nYou have selected ", destination, " as your destination.", sep = "")
    print("You're selected airline is ", airline, ".", sep = "")
    
    # Prints passenger information, using a Boolean for correct grammar.
    if (adults + minors) == 1:
        print("\nYou have selected ", adults + minors, " total passenger consisting of ", sep = "", end = "")
    else:
        print("\nYou have selected ", adults + minors, " total passengers consisting of ", sep = "", end = "")
    if adults == 1:
        print(adults, " adult and", sep = "", end = " ")
    else:
        print(adults, " adults and", sep = "", end = " ")
    if minors == 1:
        print(minors, " minor.\n", sep = "")
    else:
        print(minors, " minors.\n", sep = "")
    
    # Actual calculations based on how many adults and how many minors were entered and their corresponding ticket prices.
    print("The total airfare for adults is ", "${:,.2f}".format(airfare * adults), ".", sep = "")
    print("The total airfare for minors is ", "${:,.2f}".format((airfare * DISCOUNT)*minors), ".\n", sep = "")
    print("The total cost for the family is ", "${:,.2f}".format(((airfare * DISCOUNT)*minors)+(airfare * adults)), ".", sep = "")
    line()
    

# Starts the main function.
main()

