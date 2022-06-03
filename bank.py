from sys import exit

password = int(input("This is the account for Albert Rogö. Please type the code"))
if password == 4321:
    print("Welcome!")
else:
    print("Wrong! Try again!")
    exit()

account = 500

print("Your account has 500 dollars.")
option = input("Want to make a deposit or withdraw? D/W")

if option == "D":
    deposit = int(input("How much do you want to deposit?"))
    print("You have deposited"(deposit))
    print("Your account has a total balance of"(account+deposit))
    print("Have a good day!")
    exit()

if option == "W":
    print("Your account has a balance of"(account))
    withdraw = int(input("How much do you want to withdraw?"))
    print("You have withdrawn"(withdraw))
    print("Your account has a total balance of"(account-withdraw))
    print("Goodbye!")
    exit()
    if account > 0:
        print("You have no money left.")
        exit()