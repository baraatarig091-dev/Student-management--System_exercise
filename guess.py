number_secret = 7
guess_number = int(input("guess a number between 1 and 10: "))
while guess_number != number_secret:

    print("the number is false guess again")

    guess_number = int(input("guess a number between 1 and 10: "))
print("this is right number you are win!!")
