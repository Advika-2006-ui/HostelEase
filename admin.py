# HOSTELEASE
# Module 3: Admin Login

def admin_login():

    print("\n==================== Admin Login ====================")

    username = input("Enter your username: ")
    password = input("Enter the password: ")

    if password == "1234" and (username == "Admin" or username == "admin"):
        print("\nLogin Successful!")
    else:
        print("\nInvalid Username or Password. Try Again!")