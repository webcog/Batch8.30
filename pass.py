# import random
# lower = "qwertyuiopasdfghjklzxcvbnm"
# upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
# symbol = "~`!@#$%^&*()_-+={}[]|/.':;"
# number = "0123456789"

# all_chars = lower + upper + symbol + number
# length = 9
# password = random.sample(all_chars, length)
# o = ''.join(password)
# print(o)
# sample 

# rnadint 

# import random
# x = random.randint(1,2)
# user = input("Enter any Number Value: ")
# y = int(user)
# # 1 == "1" = false
# if y == x:
#     print("Your Guess is Right")
# else:
#     print("Your Guess is Not Correct", x)

# import time

# print("Code Strt")

# time.sleep(10)

# while True:
#     print("Hello this is While Loop")

# pyautogui     


# import pyautogui
# import time

# time.sleep(5)
# # typewrite hello
# # press "enter"
# msg = "Hello this our python class relted to modules"
# x = 1
# while x < 11:
#     pyautogui.typewrite(msg)
#     pyautogui.press("enter")
#     time.sleep(1)
#     x=x+1


# from random import randrange
# from turtle import *

# from freegames import square, vector

# food = vector(0, 0)
# snake = [vector(10, 0)]
# aim = vector(0, -10)


# def change(x, y):
#     """Change snake direction."""
#     aim.x = x
#     aim.y = y


# def inside(head):
#     """Return True if head inside boundaries."""
#     return -200 < head.x < 190 and -200 < head.y < 190


# def move():
#     """Move snake forward one segment."""
#     head = snake[-1].copy()
#     head.move(aim)

#     if not inside(head) or head in snake:
#         square(head.x, head.y, 9, 'red')
#         update()
#         return

#     snake.append(head)

#     if head == food:
#         print('Snake:', len(snake))
#         food.x = randrange(-15, 15) * 10
#         food.y = randrange(-15, 15) * 10
#     else:
#         snake.pop(0)

#     clear()

#     for body in snake:
#         square(body.x, body.y, 9, 'black')

#     square(food.x, food.y, 9, 'green')
#     update()
#     ontimer(move, 100)


# setup(420, 420, 370, 0)
# hideturtle()
# tracer(False)
# listen()
# onkey(lambda: change(10, 0), 'Right')
# onkey(lambda: change(-10, 0), 'Left')
# onkey(lambda: change(0, 10), 'Up')
# onkey(lambda: change(0, -10), 'Down')
# move()
# done()



from random import choice
from turtle import *

from freegames import square

cells = {}


def initialize():
    """Randomly initialize the cells."""
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False

    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            cells[x, y] = choice([True, False])


def step():
    """Compute one step in the Game of Life."""
    neighbors = {}

    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            count = -cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True


def draw():
    """Draw all the squares."""
    step()
    clear()
    for (x, y), alive in cells.items():
        color = 'green' if alive else 'black'
        square(x, y, 10, color)
    update()
    ontimer(draw, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
done()