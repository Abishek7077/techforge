username_password = {"Dave":"12341","john":"12342","Bob":"12343"}
name= input("Please enter your username.\n")
passcode1 =input("now enter a password .\n")

passcode=passcode1.strip()
if username_password[name]==passcode:
    print("welcome")
else:
    print("user not found")

