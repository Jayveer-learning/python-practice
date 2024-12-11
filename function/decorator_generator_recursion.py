
#? decorator 

# def decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         fun(*args, **kwargs)
#         print("Bye")
#     return wrapper

# @decorator
# def welcome(name):
#     print(f"Hello welcome {name}")
# welcome("Jayveer")


# #? recursion

# def fractional(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fractional(n-1)

# print(fractional(5)) # 120


#? generator 

#? Generator: A generator is a function that produces values one at a time using the yield statement. It doesn’t 
#? store all values in memory at once but generates them as they are requested, making it memory efficient.


#* When to use: If you need to generate values on demand, especially when working with large data sets that don’t need to be stored all at once.
def generator():
    for i in range(1, 100):
        yield i  # This generator will yield numbers from 1 to 99
# before using generator need to create instance of generator function
gen_instance = generator()

# Using next() to get the next value from the generator instance
print(next(gen_instance))
print(next(gen_instance))
print(next(gen_instance))
print(next(gen_instance))
print(next(gen_instance))
print(next(gen_instance))

# Collecting remaining generator values into a list
gen_Value_In_List = []

for gen in gen_instance: # This will continue from where the generator left off
    gen_Value_In_List.append(gen)

print(gen_Value_In_List) # Output: [7, 8, 9, ..., 99]


#? Quick Summary:
#     Iterable: An object that can return an iterator (e.g., list, string).
#     Iterator: An object that produces one value at a time using next().

# If you need on-demand data (especially with large datasets), use generators or iterators to avoid loading everything 
# into memory at once. Otherwise, use comprehensions if you need the entire dataset immediately.


#* Key Improvements:

#     Generator Instance: You correctly created the generator instance with gen_instance = generator().
#     Using next(): You used the next() function to fetch the first few values generated. Each call to next() moves the generator forward.
#     Looping through remaining values: After fetching the first few values with next(), you used a for loop to append the remaining generator 
#     values into the list gen_Value_In_List. The generator continues from where it left off, ensuring no values are missed.

# Important Notes:

# Once you call next() on a generator, it advances and retains its position. So in the loop, it continues from where the last next() call ended.
# After all values are generated, the generator will raise a StopIteration exception, and the loop will end automatically.

# Final Output:

#     First 6 values: 1, 2, 3, 4, 5, 6 (from next() calls).
#     Remaining values in the list: [7, 8, 9, ..., 99] (collected using the for loop).

# This approach demonstrates both manual control over a generator with next() and efficient collection of values into a list with a loop.
#  Well done!


#? end


# Generator Expression

# generator = (i * 5 for i in range(5) if i % 2 == 0)
# print(next(generator))
# print(next(generator))
# print(next(generator))

# # comprehension

# listComprehension = [i for i in range(10)]
# print(listComprehension)

# listCo = [i for i in range(10)]
# print(listCo)

listdata = [i * 2 for i in range(10)]
print(listdata)