import random
from random import randrange

num_of_employees = 20
# Lists of names
FIRST_NAME_LIST = ["Joshua", "Adam", "Brisa", "Zelda", "Sarah", "Henry", "Kevin",
                   "Brian", "Michael", "Lance", "Dwight", "Pamela", "Angela", "Kelly", "Oscar"]
LAST_NAME_LIST = ["Boehm", "Curry", "Smith", "Malone", "Cheek", 
                  "Scott", "Schrute", "Martinez", "Flax", "Cejudo", "Cavill", "Malone"]

# Function to randomly assign values to employee record
def generate_employee_record():
    fullname = (random.choice(FIRST_NAME_LIST) + " " + random.choice(LAST_NAME_LIST))
    employee_id = randrange(1000,9999)
    hours_worked = round(random.uniform(10,40),1)
    hourly_rate = round(random.uniform(15,100),2)
    employee_record = [employee_id, fullname, hours_worked, hourly_rate]
    return employee_record

# Open and writes data to Original.txt       
while True:
    with open("Original.txt","w") as out_original:

        # Offer to randomly generate employee records (It's a lot of typing otherwise)
        random_names_or_not = input("Do you want to randomly generate records? Y or N \t")
        print("\n")

        # User elected to have them randomly generated
        if random_names_or_not.lower() == "y":
            for emp_record in range(num_of_employees):
                for records in generate_employee_record():
                    out_original.write('%s ' % records)
                out_original.write("\n")
            print(str(num_of_employees) + " employee records were randomly generated.")
            break

        # User elected to write information themselves
        elif random_names_or_not.lower() == "n":

            # Ask for individual info 20 times.
            for employee in range(num_of_employees):

                # Employee ID number with input verification
                while True:
                    try:
                        idnumber = int(input("Enter a 4 digit ID number for employee #%s: " % employee))  
                        if idnumber in range(1000,10000):
                            out_original.write('%s ' % idnumber)
                            print("Entry accepted.\n")
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid Entry")
                        continue

                # First and last name input with input verification
                while True:
                    try:
                        first_name = input("Enter first name for employee #%s: (Must be at least 2 characters): " % employee)
                        last_name = input("Enter last name for employee #%s: (Must be at least 2 characters): " % employee)
                        if (len(first_name) >= 2) & (len(last_name) >= 2) & first_name.isalpha() & last_name.isalpha():
                            full_name = first_name.capitalize() + " " + last_name.capitalize()
                            out_original.write('%s ' % full_name)
                            print("Entry Accepted")
                            break
                        else:
                            raise TypeError
                    except TypeError:
                        print("Invalid Entry")
                        continue    

                # Weekly hours worked with input verification
                while True:
                    try:
                        weeklyhours = int(input("How many hours does employee #%s work weekly? (0-50): " % employee))  

                        if weeklyhours in range(50):
                            out_original.write('%s ' % weeklyhours)
                            print("Entry accepted.\n")
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid Entry")
                        continue

                # Hourly rate of pay with input verification
                while True:
                    try:
                        hourlyrate = float(input("What is the hourly rate of employee #%s? (0-200):" % employee))
                        if hourlyrate in range(200):
                            hourlyrate = "{:.2f}".format(hourlyrate)
                            out_original.write("%s " % hourlyrate)
                            print("Entry accepted.\n")
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid Entry")
                        continue

                # Affirmation of data recording
                print("Employee #%s's record complete.\n" % employee)
            break

        # Informs user of invalid input, continues asking for value
        else:
            print("Invalid entry")
            continue
            

# Opens Original.txt in Read mode, and the Copy.txt 
with open('Original.txt', 'r') as in_original, open("Copy.txt", "w") as copy:
    for line in in_original:
        
        # Take each value in the line as an element of a list, for easier arithmetic.
        record_as_list = line.split()
        
        # Join first and last name elements as a single element
        record_as_list[1:3] = [' '.join(record_as_list[1:3])]
        
        # Calculate gross salary with elements in employee record list
        gross_salary = (float(record_as_list[2])) * (float(record_as_list[3]))
        gross_salary = "{:.2f}".format(gross_salary)
        
        # Append gross salary to employee record list
        record_as_list.append(gross_salary)
        
        # Determine tax bracket for employee
        if float(record_as_list[4]) > 2500:
            tax = "{:.2f}".format(float(record_as_list[4]) * 0.33)
        else:
            tax = "{:.2f}".format(float(record_as_list[4]) * 0.24)
        
        # Append tax to employee record list
        record_as_list.append(tax)
        
        #Calculate net salary with elements in employee record list
        net_salary = float(record_as_list[4]) - float(record_as_list[5])
        net_salary = "{:.2f}".format(net_salary)
        
        # Append net salary to employee record list
        record_as_list.append(net_salary)
        
        # Write the appended list (with income/tax information) to the Copy file
        copy.write(" ".join(record_as_list) + "\n")

# Open the Copy.txt in a Read
with open("Copy.txt", "r") as copy:
    display = input("Would you like to read the data in a list or in blocks of plain English? (Either [list] or [english]) ")
    print("\n")
    display.lower()
    
    # Ask how the user would like to view the data
    for line in copy:
        
        # Take each value in the line as an element of a list, for easier arithmetic.
        copy_record_as_list = line.split()

        # Join first and last name elements as a single element
        copy_record_as_list[1:3] = [' '.join(copy_record_as_list[1:3])]

        # Display data as it is stored: a list.
        if display == "list":        
            print(copy_record_as_list)

        # Display data as a string in a block of English.
        elif display == "english":
                print("Employee ID: " + copy_record_as_list[0])
                print("Name: " + copy_record_as_list[1])
                print("Weekly Hours Worked: " + copy_record_as_list[2])
                print("Hourly Rate: " + "${:,.2f}".format(float(copy_record_as_list[3])))
                print("Gross Pay: " + "${:,.2f}".format(float(copy_record_as_list[4])))
                print("Tax: " + "${:,.2f}".format(float(copy_record_as_list[5])))
                print("Net Pay: " + "${:,.2f}".format(float(copy_record_as_list[6])))
                print("\n")
        
        # Input verification
        else:
            print("Invalid Entry")
            display = input("Would you like to read the data in a list or in blocks of plain English? (Either [list] or [english]) ")
            print("\n")
            display.lower()
