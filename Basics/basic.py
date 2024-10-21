# this is Comment

# print("Python is Fun!!!")
# print("Hurray")

#  Data Types String and Integer

# name = ("Darth vader")
# print(name)
# age = 19
# print(age)

# Float

# pi = (3.41)
# print(pi)
# type(pi)

# Boolean

# bool_example = True
# print(bool_example)
# type(bool_example)

# I_cannot_do_it = False
# print(I_cannot_do_it)

# Type Castng

# age = "100"
# type(age)
# print(int(age))
# height = "1.09"
# print(height)
# print(float(height))
# new_height = float(height) + 0.66
# print(new_height)

# USD to EURO Convertor

# usd_amout = 100

# exchange_rate = 0.92

# eur_amount = usd_amout * exchange_rate

# eur_amount = int(eur_amount)

# print("The Amount in EURO is:", eur_amount)

# Maths In Python
# Arthicmatic Rules

# age = 44.4
# add 1 and multiply with 2 and added in age
# print(age+1*2)

# Multiple age with 2
# print((age+1)*2)

# Power
# print((age+1)**2)

# Heights
# ahsoka_height = float(1.7)
# yoda_height = float(0.66)
# r2d2_height = float(1.09)
# c3po_height = float(1.75)
#  total variables divided by 4
# print((ahsoka_height + yoda_height + r2d2_height + c3po_height) / 4)
# String Concatination
# name = "Yoda"
# print("Your name is "+name)
# height = 0.66
# age = 900
# print("Your name, height and age is: " + name +"," + str(height) + "and age is "+ str(age))
# print(type(name))
# print(type(height))
# print(type(age))


# first_name = "Jack"
# second_name = "Rose"
# year = 1912

# print(first_name + " and " + second_name + " were on the Titanic in "+ str(year))

# Exercise
""" You are an intern at a bank and you habe been tasked to create a simple program to calculte the interest that customer will earn on their saving account. The interest is calculated yearly using the simple interest formula 

Simple interest = principal * rate * time / 100

"""
# principal = 1000
# rate = 5
# time = 2
# interest = (principal * rate * time)/100
# print(interest)

# Level 4
# Functions

# a = 1
# b = 2
# c = 3
# minimum_value = max(a, b, c)
# you can use this as well
# a,b,c =1,2,3
# print(max(a,b,c))

# a = -7.6
# Absolute Value
# a = abs(a)
# print(a)
# print(abs(-7.6))  # Output: 7.6
# round
# b = -7.6
# b = round(b)
# print(b)
# print(round(-7.6))  # Output: -8
# ashoka_height = 1.70
# yoda_height = 0.66
# r2d2_height = 1.09

# average_height = (ashoka_height+yoda_height+r2d2_height) / 3
# maximum_height = max(ashoka_height,yoda_height,r2d2_height)
# minimum_height = min(ashoka_height , yoda_height , r2d2_height)
# print("The Average Height is "+ str(average_height)+". The maximum Height is "+str(maximum_height)+ ". The Minimum Height is "+str(minimum_height))

# Input Function

# name = input("What is your Name? ")
# age = int(input("Enter your Age "))
# print("Your name is  "+ name +" and your age is " +str(age))

# Custom Functions

# def your_name_function():
#     your_name = input("What is your name? ")
#     print("Your name is "+your_name)

# your_name_function()

# def age_of_rey():
#     age = int(input("How old is Rey? "))
#     print("Rey's age is "+str(age))

# age_of_rey()  # Output: How old is Rey? Rey's age is 19

# name = input("What is his Name? ")
# age = input("What is "+name+"'s age" )

# def age_in_one_year(name, age):
#     age_next_year = int(age) + 1
#     print("In one year, "+name+" will be "+str(age_next_year)+" years old.")

# age_in_one_year(name, age)

# name = input("Who was on Titanic? ")
# year = input("What year is it? ")

# def titanic(name, year):
#     year = int(year)
#     year = year - 1912
#     year = str(year)
#     print(name + " were on the Titanic, which sunk " + year + " Years ago.")


# titanic(name, year)

# def my_age(age):
#     print("My age is " + str(age))


# my_age(39) # Output: My age is 25
# def my_age(age = 19):
#     print("My age is " + str(age))


# my_age() # Output: My age is 25

# Return Values in Function

# def convert_f_to_c(a):
#     return (a-32)/1.8


# convert_f_to_c(80)

# def convert_c_to_f(a):
#     return (a*1.8)+32


# convert_c_to_f(27)

# Function Exercise

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b


# num1 = float(input("Enter 1st Number"))
# num2 = float(input("Enter 2nd number"))

# operator = input("Enter operator (+, -, *, /): ")

# if operator == "+":
#     print("The result is: ", add(num1, num2))
# elif operator == "-":
#     print("The result is: ", sub(num1, num2))
# elif operator == "*":
#     print("The result is: ", mul(num1, num2))
# elif operator == "/":
#     print("The result is: ", div(num1, num2))
# else:
#     print("Invalid operator")  # Output: Invalid operator


# boba_fett_experience = 20
# storm_trooper_experience = 10
# expereince = [boba_fett_experience, storm_trooper_experience]
# total_experience = sum(expereince)
# print(total_experience)
# print(type(expereince))

x = 1
while x < 4 :
    print(x)
    x = x + 1