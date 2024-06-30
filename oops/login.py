
class log_in:
    def __init__(self, user, pass1):
        self.user = user
        self.pass1 = pass1
    def logg(self):
        if self.user == "Raja" and self.pass1 == "12345":
            print("Login successful")
        else:
            print("Login failed")
            print("Account Blocked")

username = input("Enter your username (Case Sensitive): ")
password = (input("Enter your password in Numbers: "))
newuser = log_in(username, password)
newuser.logg()