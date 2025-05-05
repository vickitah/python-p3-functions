#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(Naureen):
    print(f"Hello, {Naureen}!")
    
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def halve(number):
    if type(number) == int or type(number) == float:
        return number / 2
   