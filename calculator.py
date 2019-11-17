'''*********PROGRAM INTRODUCTION**************
This simple program asks the user name,age and mobile number and each of the above entries getting valid inputs
this allow the user to use various calculation operations. This app was mini-project in internship of 8th semester
BSc.CSIT students of GODAWARI CSIT COLLEGE, group-5. GROUP MEMBERS ARE Arjun Bista, Dipendra Rai and Sushan Shtestha.
We named this program a BRILLIANT-CALCULATOR APP.
Hope you will enjoy using the program.'''

#program starts here


import sys
# This is the start of the code that accept the user detail and  checks the validity of them.
name = input("enter your name:\n")
for x in range(1, 5):
    if name.isalpha() == True or ' ' in name:
        if len(name) >=3:
            print("You entered the name:", name)
            break
        else:
            print("Invalid input!!!\n   Name must be more than two alphabets!")
            name = input("Enter your name again:\n")
    else:
        print("Invalid name!!!\nName must be alphabets!")
        name = input("Enter your name again:\n")
print("\nNow time for age verification:")

age = input("Enter your age:")
for y in range(1, 5):
    if age.isdecimal() == True:
        if len(age)<3:
            if int(age) >=18:
                print("You entered the age:\n", age)
                break
            else:
                print("Invalid input!!!\nAge must be more than 18 years to be able to use this application!")
                age = input("Enter your age again:\n")
        else:
            print("Age should be less than three digit value.\n")
            age = input("Enter your age:\n")
    else:
        print("Invalid input!!!\nAge must be decimal value!")
        age = input("Enter your age again:\n")
print("\nNow time to give your mobile number:")

mobile_no =  input("Enter your mobile number:\n")
for z in range(1, 5):
    if mobile_no.isdecimal() == True:
        if len(mobile_no) ==10:
            print("Your mobile number:", mobile_no)
            break
        else:
            print("Invalid input!!!\nMobile number must be 10 digit long!")
            mobile_no = input("Enter your mobile no again:")
    else:
        print("Invalid input!!!\nMobile number must be decimal value!")
        mobile_no = input("Enter your mobile number again:")
print("You entered the following entries\nName          :", name, "\nAge           :", age, "\nMobile number :", mobile_no, "\nCongratulations!!!\nYou are now verified to use the BRILLIANT-CALCULATOR APP.")
#personal detail input and verification ends here


#block of code for calculator started here

def calculator():
    print("You can do the following mathematical operations with BRILLIANT-CALCLATOR APP")
    print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\n5.Square Root\t6.nth root\t7.Exponential\t8.Average")
    choice = int(input("Enter Your choice:\n"))
    condition = 'Y'
    while condition == 'Y':
        if choice == 1:
            decision = 0
            while decision < 1:
                list = []
                i = 0

                n = int(input("\nEnter number of elements whose sum you want to calculate:"))

                while (i < n):
                    print("enter number")
                    element = float(input())
                    list.append(element)
                    i += 1
                print(list)
                sum = 0
                for item in range(0, len(list)):
                    sum = sum + list[item]
                print("Sum of the items:", sum)
                print("Do you want to add another number?")
                add_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Addition\n\t3.Exit program"))
                if add_choice == 1:
                    calculator()
                elif add_choice == 2:
                    decision = 0
                elif add_choice == 3:
                    sys.exit("\n---------Program exiting after addition operation!!!---------")



        elif choice == 2:
            print("You choose a Subtraction.")
            decision = 0
            while decision < 1:
                first_number = input("Enter first number:\n")
                second_number = input("Enter second number:\n")
                subtraction = float(first_number) - float(second_number)
                print("Result of the subtraction operation:\n\tFinal Result=", subtraction)
                print("Do you want to subtract another number?")
                sub_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Subtraction\n\t3.Exit program"))
                if sub_choice == 1:
                    calculator()
                elif sub_choice == 2:
                    decision = 0
                elif sub_choice == 3:
                    sys.exit("\n---------Program exiting after Subtraction operation!!!---------")




        elif choice == 3:
            print("You choose a Multiplication.")
            decision = 0
            while decision < 1:
                list = []
                i = 0

                n = int(input("Enter number of elements which you want to multiply:\n"))
                while (i < n):
                    print("enter item of the list")
                    element = float(input())
                    list.append(element)
                    i += 1
                print(list)
                product = 1
                for item in range(0, len(list)):
                    product = product * list[item]
                print("Product of the numbers:", product)
                print("Do you want to multiply another number?")
                mul_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.multiplication\n\t3.Exit program"))
                if mul_choice == 1:
                    calculator()
                elif mul_choice == 2:
                    decision = 0
                elif mul_choice == 3:
                    sys.exit("\n---------Program exiting after multiplication operation!!!---------")




        elif choice == 4:
            print("You choose division operation.")
            decision = 0
            while decision < 1:
                divident = input("enter Divident:\n")
                divisor = input("Enter Divisor:\n")
                quotient = int(divident) / int(divisor)
                remainder = int(divident) % int(divisor)
                print("\nResult of the division operation:\n\tquotient       :", int(quotient), "\n\tremainder      :",
                      remainder)
                print("Do you want to divide another number?")
                div_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Division\n\t3.Exit program"))
                if div_choice == 1:
                    calculator()
                elif div_choice == 2:
                    decision = 0
                elif div_choice == 3:
                    sys.exit("---------Program Exiting after division operation!!!---------")


        elif choice == 5:
            print("You choose to calculate the Square Root\n")

            decision = 0
            while decision < 1:
                number = input("enter the number whose square root is to be calculated:\n")
                result = print("Square root:", float(number) ** (1 / 2))
                print("Do you want to calculate the square root of another number?")
                sqroot_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Square Root\n\t3.Exit program"))
                if sqroot_choice == 1:
                    calculator()
                elif sqroot_choice == 2:
                    decision = 0
                elif sqroot_choice == 3:
                    sys.exit("---------Program exiting after Square Root calculation!!!--------")


        elif choice == 6:
            print("You choose to calculate the nth root of the number")
            decision = 0
            while decision < 1:
                number = input("enter the number whose nth root is to be calculated:\n")
                nth_root = input("enter the nth root value")
                result = print("nth root:", float(number) ** (1 / float(nth_root)))

                print("Do you want to calculate the nth root of another number?")
                nroot_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.nth Root\n\t3.Exit program"))
                if nroot_choice == 1:
                    calculator()
                elif nroot_choice == 2:
                    decision = 0
                elif nroot_choice == 3:
                    sys.exit("---------Program exiting after nth root calculation!!!--------")



        elif choice == 7:
            print("You choose to calculate the exponential.\n")
            decision = 0
            while decision < 1:
                base = (input("Enter base"))
                exponent = (input("Enter exponent of base"))
                result = print("The base ", base, "and exponent", exponent, "returned the value",
                               float(base) ** float(exponent))
                print("Do you want to perform another Exponential Operation?")
                expnt_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Exponential\n\t3.Exit program"))
                if expnt_choice == 1:
                    calculator()
                elif expnt_choice == 2:
                    decision = 0
                elif expnt_choice == 3:
                    sys.exit("---------Program exiting after nth root calculation!!!--------")



        elif choice == 8:
            print("You choose to calculate average value of the numbers.\n")
            decision = 0
            while decision < 1:
                list = []
                i = 0
                n = int(input("Enter number of elements whose Average you want to calculate:"))
                while (i < n):
                    print("enter another item of the list")
                    element = float(input())
                    list.append(element)
                    i += 1
                print(list)
                sum = 0
                for item in range(0, len(list)):
                    sum = sum + list[item]
                print("The average of the numbers is:", sum / n)
                print("Do you want to perform another Average Operation?")
                avg_choice = int(input("What do you want to do?\n\t1.Menu\n\t2.Average\n\t3.Exit program"))
                if avg_choice == 1:
                    calculator()
                elif avg_choice == 2:
                    decision = 0
                elif avg_choice == 3:
                    sys.exit("---------Program exiting after Average calculation!!!--------")

        else:
            print("Invalid input!!!\nChoose integer value from 1 to 8")
            condition = 'F'

    sys.exit("\nThank you for using BRILLIANT-CALCULATOR APP\n*******************program exiting****************")
calculator()