#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"
        

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    return "It's perfect out there!"

def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
         return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

def calculator(operation, num1, num2):
    dict_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1/num2
    }

    if dict_map.get(operation, None) == None: print("Invalid operation!")

    return dict_map.get(operation, None)

