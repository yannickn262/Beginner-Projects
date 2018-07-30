from datetime import datetime
correct_password = "freud"
name = input("Enter Name: ")
lastname = input("Enter lastname: ")
password = input("Enter password: ")

while password != correct_password:
    password = input("Wrong password! Try again: ")

#print("Welcome", name, "you are logged in")
#instead of separating the strings, use string formatting to put them all in one
print("Welcome %s %s you are logged in" % (name,lastname))
