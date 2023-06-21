# import turtle
# turtle.speed(0)
# t = turtle.Turtle()
# turtle.bgcolor("green")
# turtle.speed(0)

# for i in range(50):
#     for colors in ["red", "magenta", "blue"]:
#         turtle.color(colors)
#         turtle.pensize(3)
#         turtle.left(12)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)

''' Randomisation in python '''
'''I will research about pseudorandom number generators
askpython.com'''
import random
random_integer = random.randint(100,500)
print(random_integer)


random_float = round(random.random(),2)
final_result_of_random_float = random_float * 5
print(final_result_of_random_float )
# 
# import mydoculs as md
# a = md.pi
# print(a)

lover = input("Enrer your girlfriend or boyfriend name")
your_name = input("Enter Your name")
love_score = random.randint(1,100)
print(f"Your Love Score is {love_score}%")

