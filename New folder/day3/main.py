# Conditional statement 
water_level = 50

if water_level > 80 :
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollecoaster!")
height = int(input("what is your height in cm?"))

totalbill = 0

if height >= 120:
    print("You can ride the rollecoaster!")
    age = int(input("Enter your age!"))
    if age < 12:
        totalbill += 5
        photos = input("You want to photos 'Yes' or 'No'")
        if photos == "Yes" or photos == "yes":
            totalbill += 3
            print(f"The total bill is : {totalbill}")
        elif photos == "No" or photos == "no":
            print(f"The total bill is : {totalbill}")      
    elif age < 18:
        totalbill += 15
        photos = input("You want to photos 'Yes' or 'No' ")
        if photos == "Yes" or photos == "yes":
            totalbill += 3
            print(f"The total bill is : ${totalbill}")
        elif photos == "No" or photos == "no":
            print(f"The total bill is : {totalbill}")  
    elif age < 22:
        totalbill += 18
        photos = input("You want to photos 'Yes' or 'No'")
        if photos == "Yes" or photos == "yes":
            totalbill += 3
            print(f"The total bil is :{totalbill}")
        elif photos == "No" or photos == "no":
            print(f"The total bill is : {totalbill}")
    elif age >= 45 and age  <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        totalbill += 20
        photos = input("You want to Photos 'Yes' or  'No'")
        if photos == "Yes" or photos == "yes":
            totalbill +=3
            print(f"Total bill is : {totalbill}")
        elif photos == "No" or photos == "no":
            print(f"The total bill is : {totalbill}")
        print("Please pay 20$")
else:
    print("Sorry, you have to grow taller before you can ride")



