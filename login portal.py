def login():
    username = input("Enter username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "123":
        print("WELCOME, ADMIN!!")
    else:
        print("INVALID USERNAME OR PASSWORD")

def account():
    print("Please enter valid details")
    gmail = input("Enter your mail: ")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    password = input("Create your Password (Length must be 7 or greater): ")

    if len(password) >= 7:
        print("Password is strong")
    else:
        print("Password is weak. It should be 7 characters or longer.")

    if '@' in gmail:
        print("Email is valid")
    else:
        print("Email is invalid. It should contain '@'.")

while True:
    print("For Exit press 'exit'")
    print("1. Login")
    print("2. Don't have an account? Create Account")
    choice = input("Enter choice (1/2/exit): ")

    if choice == '1':
        print("For now you can login as Admin!")
        login()
    elif choice == '2':
        print("By following the steps you can create your account!")
        account()
        print("Account Created!")
    elif choice.lower() == 'exit':
        print("EXIT")
        break
    else:
        print("Invalid choice. Please try again.")
