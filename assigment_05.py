Pizza = input("What size pizza do you wnat ? S, M, L ")
pizza_amount = 0
if Pizza == "S" or Pizza == "s" or  Pizza == "Small" or Pizza == "small":
    pizza_amount = 15
    pepperoni = input("Do you want Pepperoni ? 'Yes' or 'No'")
    if pepperoni == "Yes" or pepperoni == "yes":
        pizza_amount +=2
    extra_cheese = input("Do you want extra cheese? 'Yes' or 'No'")
    if extra_cheese == "Yes" or extra_cheese == "yes":
        pizza_amount +=1
    print(f"Your final bill is {pizza_amount}")   
elif Pizza == 'M' or Pizza == "m" :
    pizza_amount = 20
    pepperoni = input("Do you want Pepperoni ? 'Yes' or 'No'")
    if pepperoni == "Yes" or pepperoni == "yes":
        pizza_amount +=3
    extra_cheese = input("Do you want extra cheese ? 'Yes' or 'No'")
    if extra_cheese == "Yes" or extra_cheese == "yes":
        pizza_amount +=1
    print(f"Your final bill is {pizza_amount} ")
elif Pizza == "L" or Pizza == "l":
    pizza_amount = 25
    pepperoni = input("Do you want  Pepperoni ? 'Yes' or 'No'")
    if pepperoni == "Yes" or pepperoni == "yes":
        pizza_amount +=3
    extra_cheese = input("Do you want extra cheese ? 'Yes' or 'No'")
    if extra_cheese == "Yes" or extra_cheese == "yes":
        pizza_amount +=1
    print(f"Your final bill is ${pizza_amount}")
else:
    print("Plese Enter input in Yes or No !")



#                                       Or
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizza_amount = 0
if size == "S" or size == "s" or  size == "Small" or size == "small":
    pizza_amount = 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        pizza_amount +=2
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_amount +=1
    print(f"Your final bill is ${pizza_amount}")   
elif size == 'M' or size == "m" :
    pizza_amount = 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        pizza_amount +=3
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_amount +=1
    print(f"Your final bill is ${pizza_amount} ")
elif size == "L" or size == "l":
    pizza_amount = 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        pizza_amount +=3
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_amount +=1
    print(f"Your final bill is ${pizza_amount}")
else:
    print("Plese Enter input in Yes or No !")




