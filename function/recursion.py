# factorial(6) = 6 * 5 * 4 * 3 * 2 * 1 = value of this is factorial of 6
# factorial(7) = 7 * 6 * 5 * 4 * 3 * 2 * 1 = value of this is factorial of 7
# factorial(5) = 5 * 4 * 3 * 2 * 1 = value of this is factorial of 5
# factorial(6) = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = value of this is factorial of 8


# calculating factorial using recursion function :-
# formula is :- factorial(n) = n * factorial(n - 1)  :- so if n is 5 n - 5 means 5 - 1 = 4 so 
#  n * factorial(n - 1)  5 * factorial(4-1)

# and 0=1, 1=1
# formula of factorial :- n * f(n-1) 

# factorial(0) is 1 and factorial(1) is 1 then factorial(2) = 2 * 1 = 3 like that but 0=1, 1=1

# recurtion 

def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1) # this is recursion function call itself in owne body but 

print(factorial(5))

# 120 factorial of 5 is 120

# recursion function means aise function jo apne apko hi apna function body ma call karta ho but defirent
# arragument ka sath. for ex. like that factorial(n-1) new argument is n-1


# Fibonacci sequence 
# f(0) = 1
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(f-2)   # for ex. if n is 5 so =
#  f(n-1) measn f(5-1) = 4 and f(n-2) means f(5-2) = 3 || f(5-1) = 4 + f(5-2) = 3 = 7 fibonacci of 5

# formula of Fibonacci reule :-
# f(n) = f(n-1) + f(n-2) 

# To calculate Fibonacci(8), we will follow the Fibonacci formula:

#     F(n) = F(n-1) + F(n-2)

# We already know the values for smaller Fibonacci numbers:

#     F(0) = 0
#     F(1) = 1
#     F(2) = 1
#     F(3) = 2
#     F(4) = 3
#     F(5) = 5
#     F(6) = 8
#     F(7) = 13

# f(8) = f(8-1) = 7 + f(8-2) = 6
# f(8) = f(13) + f(8) = 21 Fibonacci of 8 is 21 
# finonacci no. are calculate using privious Fibonacci no. for ex. fiboracci
# no. of 7 is 13 and fibonacci of 6 is 8 so .-> fobinacci of 8 is 8 is using formula
# f(8-1) = 7 + f(8-2) = 6 => 13 + 8 = 21 is fibonacci of 8.

# So if you want to calculate Fibonacci of any n no. so first you no previous 
# fibonacci no. of n then using. need n of n-1 + n-2 know this two fibonacci
# no. for calculating this n no. of fibonacci.

# create fibonacci

# F(0) = 0
# F(1) = 1

def Fibonacci(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2) # using recursion function
    
print(Fibonacci(8)) # -- > Fibornacci of 8 is 21
