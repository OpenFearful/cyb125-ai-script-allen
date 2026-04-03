password_score = 0
import re

#Function to check a user's given password
def passwordcheck(passcheck):
    input("Press -Enter- to see your password strength. ")
    password_score = 0
    #Higher Security Points for length
    if len(passcheck) >= 5:
        password_score += 1
    elif len(passcheck) >= 7:
        password_score += 2
    elif len(passcheck) >= 9:
        password_score += 2
    else:
        password_score -= 1

    #Checks if the password is either all upper or lowercase
    if passcheck != passcheck.lower():
        password_score += 1
    elif passcheck != passcheck.upper():
        password_score += 1
    #Checks to see if the user password contains at least one number
    if re.search(r'\d', passcheck):
        password_score +=3
    else: 
        password_score += 0

    #Another check to see if the password contains any special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', passcheck):
        password_score += 2
    else:
        password_score += 0
    
    #This is where the function calculates the password strength relative to the points they accumulated prior
    if password_score <= 3:
        return "Your password is weak."
    elif password_score >= 5:
        return "Your password is very strong!"

#Gets user password, calls the function, then prints the password strength
password = input("What is the password you want to check? ")
choice = input(f"Your password is {password}. Continue? (y/n) ").lower()
if choice.startswith('y'):
    check = passwordcheck(password)
    print(check)
else:
    password = input("What is the password you want to check? ")
    check = passwordcheck(password)
    print(check)
    



        
        