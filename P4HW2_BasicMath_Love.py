# create a program that display a menu
# CTI-110
# P4HW2 - BasicMath
# july 3 2020
# Carlando Love


def main():
    keep_going = 'yes'
    while (keep_going.upper() == 'YES'):
        # print menu
        print('\nMenu')
        print('  1. Add Numbers')
        print('  2. Multiply Numbers')
        print('  3. Subtract Numbers')
        print('  4. Exit Program\n')
        choice = int(input('Please enter your choice: '))

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        


        #get choice
        if choice == 1:
            #Adition
            print (num1, "+", num2, "=", num1+num2)
            
        elif choice == 2:
            #Multiply
            print (num1, "*", num2, "=", num1*num2)
            
        elif choice == 3:
            #Subtract
            print (num1, "-", num2, "=", num1-num2)
            
        elif choice == 4:
            #exit program
            print('Choice was 4.  Exiting program')
            keep_going = 'n'
        else:
            #invalid entry
            print('Choice was not valid.  Please choose a valid option.')
            input('Press any key to continue.')



main()
