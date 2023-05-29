# this is a password guesser - not hacker


import random

password = input("Enter a password:")

length = len(password)
print(length)
 #acdii
random_num = "123456789"


guessed = " "
while password != guessed:
    guessed = random.choices(random_num, k=length)
    print("<======= "  + str(guessed) + " ======>")
    if guessed == list(password):
        print("Your password is: " + "".join(guessed))
        input()
        break
