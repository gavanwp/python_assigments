print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lover_case = name1.lower() + name2.lower()

T = lover_case.count("t")
R = lover_case.count("r")
U = lover_case.count("u")
E = lover_case.count("e")


true = T+R+U+E

l = lover_case.count("l")

o = lover_case.count("o")

v = lover_case.count("v")

i = lover_case.count("e")


Love = l+o+v+i

Love_Scores = str(true) +  str(Love)
# Love_Scores = int(str(true) + str(Love))



if int(Love_Scores) <= 10 or int(Love_Scores) >= 90:
    print(f"Your score is {Love_Scores}, you go together like coke and mentos.")
elif int(Love_Scores) >= 40 or int(Love_Scores) <= 50:
    print(f"Your score is {Love_Scores}, you are alright together.")
else:
    print(f"Your score is {Love_Scores}.")









