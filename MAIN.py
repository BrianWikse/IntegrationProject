#My name is Brian Wikse

#This is a quiz game.

#This is a function that will print a name and email when it is called, this function is used in Quesion 10.
def info(name, mail):
    print(name, mail)

print("Welcome to", end=' ')
print("the Quiz Game!")
#The end= in the print statement combines the two print statements and adds a space between the two statements
print("This program was finished on:")
print('10','24','2020', sep='/')
#The sep= in the print statement changes the normal space separator to a "/".

score = 0
#Sets the variable score's value to 0.

question1 = int(input("\nWhat is 2 + 1?  "))
#The "+" allows the program to add 1 to 2 in order to get the answer of 3.
if question1 == (2+1):
    score+=1
    #Adds 1 to the variable score's value.
    print("Correct!")
elif question1 != (2+1):
    print("Incorrect!")
                
question2 = int(input("\nWhat is 1,730 - 393?  "))
#The "-" allows the program to subtract 393 from 1730 to get the answer of 1337.
if question2 == (1730-393):
    score+=1
    print("Correct!")
elif question2 != (1730-393):
    print("Incorrect!")
    
question3 = int(input("\nWhat is 54 * 17?  "))
#The "*" allows the program to multiply 54 and 17 to get the answer of 918.
if question3 == (54*17):
    score+=1
    print("Correct!")
elif question3 != (54*17):
    print("Incorrect!")
    
question4 = int(input("\nWhat is 1422 / 9?  "))
#The "/" allows the program to divide 9 from 1422 to get the answer of 158.
if question4 == (1422/9):
    score+=1
    print("Correct!")
elif question4 is not 158:
    print("Incorrect!")
#The "not" operator works the same as using !=.

question5 = int(input("\nWhat is 4 to the power of 4?  "))
#The "**" allows the program to put 4 to the power of 4 to get the answer of 256.
if question5 == (4**4):
    score+=1
    print("Correct!")
elif question5 != (4**4):
    print("Incorrect!")

question6 = int(input("\nWhat is 50 divided by 3 rounded down to the nearest whole number?  "))
#The "//" allows the program to divide 50 by 3 and then rounds down the answer to the nearest whole number which would be 16.
if question6 == (50//3):
    score+=1
    print("Correct!")
elif question6 != (2+1):
    print("Incorrect!")

question7 = int(input("\nWhat is the remainder of 170 divided by 4?  "))
#The "%" allows the program to take the remainder of 170 divided by 4.
if question7 == (170%4):
    score+=1
    print("Correct!")
elif question7 != (170%4):
    print("Incorrect!")

print("\nIf you wanted to count from 1 to 10 in python, which line of code would you use?")
print("A: for num in range(1, 11):")
print("B: for num in range(10):")
print("C: for num in range(1, 10, 1):")
print("D: None of the above.")
question8 = str(input("What is your answer?  "))
if question8 == "A" or question8 == "a":
    score+=1
    print("Correct! Here is the result of the code: ")
    for num in range(1, 11):
        print(num)
#The for loop uses in and range as paramaters for the loop.
#The code will print from the number 1 to the number 10 because our range starts at 1 and ends at 11, because the range always needs to be 1 number higher then where you want it to stop.
elif question8 != "A" and question8 != "a":
    print("Incorrect! The answer was A. Here is the result of the code in A: ")
    for num in range(1, 11):
        print(num)

print("\nIf you wanted to count from 1 to 10 if num=1 in python, which line of code would you use?")
print("A: while (num>10):")
print("B: while (num>11)")
print("C: while (num>11):")
print("D: None of the above")
question9 = str(input("What is your answer?  "))
if question9 == "C" or question9 =="c":
    score+=1
    print("Correct! Here is the result of the code:  ")
    num = 1
    while (num < 11):
        print(num)
        num = num +1
#The "while" loop allows the program to keep printing the variale num until num reaches 11 which breaks the loop.
elif question9 != "C" and question9 != "c":
    print("Incorrect! The answer was C. The result of C's code would look like this: ")
    num = 1
    while (num < 11):
        print(num)
        num = num + 1

print("\nWhich function would you use if you wanted to display your name and e-mail?"  )
print("A: info(name, mail):")
print("B: def info(name, mail):")
print("C: def info(name):")
print("D: None of the above")
question10 = str(input("What is your answer?  "))
if question10 == "B" or question10 == "b":
    score+=1
    print("Correct! Here is the result of the code: ")
    info("Brian", "bjwikse9764@eagle.fgcu.edu")
else:
    print("Incorrect! The answer was B. Look at the result of B's code: ")
    info("Brian", "bjwikse9764@eagle.fgcu.edu")

if score == 10:
    score = str(score)
    print("\nYour score is: " + score + "\nExcellent! You got them all correct!")
#The "+" in the print command combines the seperate strings in order to form one complete string.
elif score <= 9 and score > 7:
    score = str(score)
    print("\nYour score is: " + score + "\nGreat job!")
elif score <= 7 and score > 5:
    score = str(score)
    print("\nYour score is: " + score + "\nPretty good job!")
elif score == 5:
    score = str(score)
    print("\nYour score is: " + score + "\nOnly half right?")
elif score < 5 and score >= 3:
    score = str(score)
    print("\nYour score is: " + score + "\nYou could have done better.")
else:
    score = str(score)
    print("\nYour score is: " + score + "\nSeriously?! Did you even try?")

score = int(score)
goodbye = ("Goodbye " * score)
#The "*" in the goodbye variable will make it so the word "Goodbye" will be printed the amount of times as the number of points the player scored when the goodbye variable is printed.
print(goodbye)        
