# def my_decorator(my_OriginalFunction):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         my_OriginalFunction(*args, **kwargs)
#         print("End")
#     return wrapper

# @my_decorator
# def hello():
#     print("Hello! I am Here")

# hello()


# A decorator in Python is a function that allows you to modify or enhance the behavior 
# of another function or method without changing its actual code. Decorators are often 
# used to add functionality like logging, authentication, timing, or caching to existing
# functions How a Decorator Works

# A decorator wraps a function inside another function, allowing you to execute code 
# before and/or after the original function runs, while maintaining the original 
# function's behavior.

# Basic Structure of a Decorator:

# A decorator is usually a function that takes another function as an argument, 
# defines a wrapper function inside, and returns the wrapper. Here's the basic pattern:

# python

# def decorator_function(original_function):
#     def wrapper_function():
#         # Code to run before the original function
#         print("Before the function runs")
        
#         original_function()  # Calling the original function
        
#         # Code to run after the original function
#         print("After the function runs")
        
#     return wrapper_function

# Example of Using a Decorator:

# python

# def decorator_function(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper

# @decorator_function
# def say_hello():
#     print("Hello!")

# say_hello()

# Output:

# r

# Before the function call
# Hello!
# After the function call

# How it Works:

# @decorator_function is placed above the say_hello function. This tells Python to 
# pass say_hello into decorator_function.
# Inside decorator_function, the wrapper function is defined, which


# decorator 

# def newDecorator(fun):
#     def wrapper():
#         print("Hello! It's start")
#         fun()
#         print("Bye! It's End")
#     return wrapper

# @newDecorator # Adding decorator in welComeFun
# def welComeFun(name = "Username"):
#     print(f"Welcome {name}")

# welComeFun()

# decorator work as ::after ::before like.


# recursion

def fraction(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fraction(n-1)

print(fraction(5)) #120 so recursion 
