#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
greet("Barack")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
# greet_with_default()
greet_with_default("Lapilly")

def add(num1, num2):
    return num1 + num2
print(add)
add(4, 5)    

def halve(number):
    return number/2
print(halve)
halve(8)