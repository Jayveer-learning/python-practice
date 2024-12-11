# lambda

# syntax : lambda argument: expression

# lambdaData = lambda x : x * x 
# print(lambdaData(5)) # --> 25

# # map() --> cude a listData by appling function on each element of iterable collection like list, tuple

# # syntax : map(function, iterable)

# listData_Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# CudeOdListData = map(lambda x : x*x*x, listData_Num)
# print(list(CudeOdListData)) # --> [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]




# filter() --> filter even cude number

# syntax : filter(function, iterable)

# re-create map  CudeOdListData 
# CudeOdListData = map(lambda x : x*x*x, listData_Num)

# evenCudeNum = filter(lambda x : x % 2 == 0, CudeOdListData)
# print(list(evenCudeNum)) # --> [8, 64, 216, 512, 1000]


#* discreption

# The issue you're encountering with filter() is likely due to the fact that the map() function
#  returns an iterator, and once you've consumed it (in your case, when you converted it to a 
#  list with print(list(CudeOdListData))), it can't be reused in the filter() function.

# Iterators are "one-time use," meaning that once you have iterated over them (e.g., by 
# converting them to a list), you need to recreate them if you want to iterate again.

# To fix this, you can either recreate the CudeOdListData iterator before using filter(), 
# or you can avoid converting it to a list until after filtering.



# reduce() --> reduce a numeber of filetr 

# syntax : recuce(function, iterable)

# re-creating a filter map() agian for reduce because. filter the CudeOdLusrData if 
# cude % 2 == return 0 then return in filter and filter store in evenCodeNum variable 
# but i well convert the iterable data why i say iterable data becuse map() filter() they return 
# iterable data. so i convert filter data into list so i convert iterable data into list
# so i use one time and [python] have rule is we can use olny one-time use iterable data
# so that way we re-create again map() and filter().
# we have one solution is we directly filter() and map() data in list we can use multiple
# time like : list(map) list(filter) no need to convert map, or filter into any collection
# and we can use many time becuase map() return map() object and filter return filetr objetc 
# so need to convert but if we store data in list so no need to convert data into any colletion 
# data type also we can this like varible_name = list(writeVarieble_Name_where_storeData)

# evenCudeNum = [8, 64, 216, 512, 1000]

# Step 3: Convert the filtered result to a list (so it can be used multiple times)

# after using reduce we need to import reudce from funtools
# from functools import reduce
# reduceTheEvenNo = reduce(lambda x, y : x + y, evenCudeNum)# --> x is accum that storeData and 
# # y this current element iteration.
# print(reduceTheEvenNo) # --> 1800


# recurtion 

# factorial
# def factorial(n) -> int:
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5)) # -> 120

# recurtion function terminate when condtion got base condtion on this code is base condition is 0 or 1 is bye if factorial 
# is 0 or 1 so if condition return the 1 and function is exited in other language fun. is terminated


# fibonacci no

# def Fibonacci(n) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         Fn = Fibonacci(n-1) + Fibonacci(n-2)
#         return Fn

        # we have to option first is return directly like tha return Fibonacci(n-1) + Fibonacci(n-2)
        # and second is using full formula first store Fibonacci(n-1) + Fibonacci(n-2) in Fn varibel or 
        # then return the Fn both are work same formula same but writing style is diffenrent. 

# print(Fibonacci(8)) # --> 21 is Fibonacci of 8th sequance

# What is the Formula for the nth Term of The Fibonacci Sequence? The formula to find the nth term of the 
# sequence is denoted as Fn = Fn-1 + Fn-2, where n >1.


# Decorato 
# changeStyleOfFunctionDynamicly is a decorator 

# def changeStyleOfFunctionDynamicly(function) -> str:
#     def wrapper(*args, **kwargs) -> None:
#         print("Start")
#         function(*args, **kwargs)
#         print("End")
#     return wrapper

# @changeStyleOfFunctionDynamicly
# def welcome(user: str) -> None:
#     print(f"Hello {user}")  

# welcome("jayveer")
# output :
# Start
# Hello jayveer
# End


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


# Node of decorator :

# Certainly! The wrapper function is a crucial part of how decorators work in Python. It allows you to extend or 
# modify the behavior of the original function while maintaining its core functionality. Here’s a detailed 
# explanation of why we use a wrapper function and how it operates:

# Purpose of the Wrapper Function

#     Enhance Functionality:
#         The primary purpose of a wrapper function is to add new behavior to the original function without 
#         modifying its code. This can include logging, authentication, timing, or any other additional behavior 
#         that you want to execute before or after the original function runs.

#     Maintain the Original Function’s Behavior:
#         The wrapper function can call the original function, allowing it to execute as intended. This 
#         ensures that the core functionality remains unchanged while adding new behavior around it.

#     Access Arguments and Return Values:
#         The wrapper can access the arguments passed to the original function and can also capture its return 
#         value. This is useful for cases where you want to manipulate or log inputs/outputs.

#     Code Reusability:
#         By using a decorator with a wrapper, you can apply the same additional behavior to multiple functions 
#         without repeating code. This leads to cleaner and more maintainable code.


# Example Breakdown

# Let’s break down the example you prevous decorator code:

#     changeStyleOfFunctionDynamicly:
#         This is the decorator function that takes an original function as an argument.

#     wrapper(*args, **kwargs):
#         This is the wrapper function defined inside the decorator. It can accept any number of positional 
#         (*args) and keyword arguments (**kwargs).

#     Before the Original Function Call:
#         print("Start") executes before the original function. This is where you can include any behavior you want
#         to occur prior to the main functionality.

#     Calling the Original Function:
#         function(*args, **kwargs) calls the original function, passing in the arguments. By unpacking args and 
#         kwargs, the wrapper allows the original function to operate with the same inputs it was designed to handle.

#     After the Original Function Call:
#         print("End") executes after the original function has finished executing. This allows you to add any
#          cleanup, logging, or additional behavior that should occur after the main functionality.

# Benefits of Using a Wrapper Function

#     Separation of Concerns:
#         The wrapper function helps separate the additional behavior from the original function, making the 
#         code cleaner and easier to manage.

#     Flexibility:
#         You can easily modify, add, or remove the behavior in the wrapper without changing the original 
#         function's code.

#     Reusable Logic:
#         The same wrapper can be applied to multiple functions, promoting code reuse.



# Here’s an example of using the wrapper to log execution time for any function:

import time

def time_logger(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time before calling the function
        result = function(*args, **kwargs)  # Call the original function
        end_time = time.time()  # End time after the function call
        print(f"Execution time: {end_time - start_time} seconds")  # Log the execution time
        return result  # Return the original function’s result
    return wrapper

@time_logger
def my_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(my_function(1000000))  # Call the function to see the logging in action


def name(name) -> None:
    print("hello", name)

name("jayveer")

name1 = input("name")
print(name1)

