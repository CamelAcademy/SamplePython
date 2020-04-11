# Learn Try Catch Exceptions
try:
    value = 10/1
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide by Zero") # 1st way to display the error
except ValueError as err:
    print(err) # 2nd way to display the error
except:
    print("Invalid Input")