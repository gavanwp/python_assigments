# Conditional statement 
water_level = 50

if water_level > 80 :
    print("Drain water")
else:
    print("Continue")


print("Welcome to the rollecoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("You can ride the rollecoaster!")
    age = int(input("Enter your age!"))
    if age < 12:
        print("Please pay 9$")
    elif age < 18:
        print("Please pay 15$")
    elif age < 22:
        print("Please pay 18$")
    else:
        print("Please pay 20$")
else:
    print("Sorry, you have to grow taller before you can ride")


