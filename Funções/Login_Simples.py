user = input("Login: ")
pw = input("Password: ")

if user == "Admin" and pw == "1234":
    print("Allowed")
else:
    print("Not Allowed")