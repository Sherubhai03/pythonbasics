class bank:
    def __init__(self, username, pass1):
        self.user = username
        self.pass1 = pass1

    def logg(self):
        if self.user == "Raja" and self.pass1 == "12345":
            print("Login successful")
            print("Welcome Raja")
            print("Your account balance is 10000")
            print("Do you want to withdraw or deposit?")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    withdraw = int(input("Enter the amount to withdraw: "))
                    if withdraw > 10000:
                        print("Insufficient balance")
                    else:
                        print("Withdrawal successful")
                        print("Your remaining balance is", 10000 - withdraw)
                        print("Thank you for using our service")
                case 2:
                    deposit = int(input("Enter the amount to deposit: "))
                    print("Deposit successful")
                    print("Your updated balance is", 10000 + deposit)
                    print("Thank you for using our service")
                case 3:
                    print("you Account Balance is 10000")
                case 4:
                    print("You are successfully logged out")
                    print("Thank you for using our service")
                case _:
                    print("Invalid choice")
        else:
            print("Login failed")
            print("Account Blocked")


newuser = bank(input("Enter your username: "), input("Enter your password: "))
newuser.logg()
