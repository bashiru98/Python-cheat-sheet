#simple python cheat sheet 


#Dictionaries    
              ex
                      age = { "bash": 20, "ali": 15}
                      print(age["bash"])
NOTE: Dictionaries are accessed by their keys
for example age.keys() 




#funtions

                passwords generator
                def password(length):
                    pW = str()
                    characters = "sffgawgsffeafsfg"
                    for x in range(length):
                        pw = pw + random.choice(characters)
                    return pw


pirnt(password(any number of choice))


#Another
            def intersection(a, b):
                res = []
                for x in a:
                    if x in b
                     res.append(x)
                return res

print(intersection([1 ,3, 4, 3, 5 ,9], [3, 7,5, 4,0]))



#For mathematical calculations
                          
                             import math
                             x = [2, 4, 5, 3, 6]
                             y = [5, 7, 2, 3, 5, 6, 6, 8, 3] 

for mean of x
     print(x.mean())
for mean of y
print(y.mean())


another
         import math
print(math.pi)


import random
            print(random.choice("maradona"))



FOR AND WHILE LOOPS


lets say names = [ 'bashiru', 'asaan', 'bukari' ]
         for name in names:
print(name)

also 
       for x in range(22):
print(x)

          age = { 'bashiru': 21, 'bukari': 33, 'asaan': 25, 'rabiatu': 18 }
          for x in age.keys:
              print(x, age[x])
NOTE: sorted can be  used to print the dictionary keys in an alphabetical order.
and sorted(age.keys()), reverse=True): will reverse the dictionary keys.

 numbers = range(10)
 squares = []
 for number in numbers:
     square = number**2
     squares.append(square)

print(squares)

for while loops
                    x = 10
            while x <= 100:
                  x += 1

                  print(x)






import numpy as np

# sigmoid function to normalize inputs
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# sigmoid derivatives to adjust synaptic weights
def sigmoid_derivative(x):
    return x * (1 - x)

# input dataset
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

# output dataset
training_outputs = np.array([[0,1,1,0]]).T

# seed random numbers to make calculation
np.random.seed(1)

# initialize weights randomly with mean 0 to create weight matrix, synaptic weights
synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

# Iterate 10,000 times
for iteration in range(10000):

    # Define input layer
    input_layer = training_inputs
    # Normalize the product of the input layer with the synaptic weights
    output = sigmoid(np.dot(input_layer, synaptic_weights))

    # how much did we miss?
    error = training_outputs - output

    # multiply how much we missed by the
    # slope of the sigmoid at the values in outputs
    adjustments = error * sigmoid_derivative(output)

    # update weights
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic weights after training: ')
print(synaptic_weights)

print("Output After Training:")
print(output)

creating a simple python calculator with some few python codes

# Python program to  create a simple GUI  
# calculator using Tkinter 
  
# import everything from tkinter module 
from tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="light green") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("265x125") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    # start the GUI 
    gui.mainloop() 





 Python program for simple calculator 
  
# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n" \ 
        "1. Add\n" \ 
        "2. Subtract\n" \ 
        "3. Multiply\n" \ 
        "4. Divide\n") 
  
  
# Take input from the user  
select = input("Select operations form 1, 2, 3, 4 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 


gravity game

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


simple chatroom

import time, socket, sys
print('Setup Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
whileTrue:
   message = input('Me > ')
   if message == '[bye]':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)


simple emoji symbols in python

from emoji import emojize
print(emojize(":thumbs_up:"))
print(emojize(':thumbs_down:'))

how to def�ne and know the meaning the codes by run

import inspect

print(inspect.getsource(inspect.getsource))
print(inspect.getmodule(inspect.getmodule))
print(inspect.currentframe().f_lineno)


welcome code

cities = ['London', 'Dublin', 'Oslo']

def visit(city):
    print("Welcome to "+city)
for city in cities:
    visit(city)

how to pr�nt onl�ne learn�ng centers centers l�nks in python visual environmtment 

import wikipedia

results = wikipedia.page('freecodecamp')
print(results.summary)

for link in results.links:
    print(link)

s�mple code for fab�nacc� numbers

# Function for nth Fibonacci number

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(9))

# This code is contributed by Saket Modi 



python code to geranerate random str�ngs t�ll geek appears

# Python program to generate and match
# the string from all random strings
# of same length

# Importing string, random
# and time modules
import string
import random
import time

# all possible characters including
# lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'


# string to be generated
t = "geek"

# To take input from user
# t = input(str("Enter your target text: "))

attemptThis = ''.join(random.choice(possibleCharacters)
                      for i in range(len(t)))
attemptNext = ''

completed = False
iteration = 0

# Iterate while completed is false
while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    # Fix the index if matches with
    # the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

            # increment the iteration
    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)

# Driver Code
print("Target matched after " +
      str(iteration) + " iterations")

code for plott�ng graphs �n pythons 

# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3]
# corresponding y axis values
y = range(2, 5)

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
print(plt.show())

plott�ng h�stogram �n python for know data

import matplotlib.pyplot as plt 
  
# frequencies 
ages = [2,5,70,40,30,45,50,45,43,40,44, 
        60,7,13,57,18,90,77,32,21,20,40] 
  
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
  
# plotting a histogram 
plt.hist(ages, bins, range, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
  
# x-axis label 
plt.xlabel('age') 
# frequency label 
plt.ylabel('No. of people') 
# plot title 
plt.title('My histogram') 
  
# function to show the plot 
plt.show() 

code or plot�ng bar chart in pyhon 

# in here we are going to plot a bar chart with simple commands in  python
import matplotlib.pyplot as plt

# lets first of all specify the left part of the bar chart
left = [1, 2, 3, 4, 5]
# height of bars
heights = [10, 24, 36, 40, 5]
# lets make some tick labels for our left values
tick_label = ["one", "two", "three", "four", "five"]

# lets now plot our bar chart
plt.bar(left, heights, tick_label= tick_label, width = 0.8, color = ["red", "green"])

# now lets name our axis

plt.ylabel("y - axis")
plt.xlabel("x - axis")

# finally we gonna show our barchart

plt.show()

scatter plot 

import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y-axis values 
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

# plotting points as a scatter plot
plt.scatter(x, y, label="stars", color="green",
            marker="*", s=30)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()


pie chart 

import matplotlib.pyplot as plt 
  
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
# plotting legend 
plt.legend() 
  
# showing the plot 
plt.show()

spirals

import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t, size)
        t.right(360/repeat)
drawSpecial(Terry, 100, 10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10) 



         