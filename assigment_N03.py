# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = weight/(height**2)
final_result = round(result)
if result < 18.5 :
    print(f"Your BMI is {final_result}, you are underweight.")
elif result < 25 :
    print(f"Your BMI is {final_result}, you have a normal weight.")
elif result < 30:
    print(f"Your BMI is {final_result}, you are slightly overweight.")
elif result < 35:
    print(f"Your BMI is {final_result}, you are obese.")
else:
    print(f"Your BMI is {final_result}, you are clinically obese.")