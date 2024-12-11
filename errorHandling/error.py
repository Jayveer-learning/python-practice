# Try block
# Programmers write main code in the try block.

# Except block
# Python executes the except block if things went wrong.

# try:
#   body of try write main code
# except:  
    # body of except write code if error in try


# Else Block :
# The function of keyword else is to define a block. This 
# block will be executed if no error occurs.

# try:
#     #body of try block
# except :
#     #body of except block
# else:
#     #body of else block



# Finally Block :
# The keyword finally will also create a block. This block will be executed
# regardless the error occur or not by try block

# try:
#     #body of try block
# except :
    #body of except block
# else:
#     #body of else block
# finally:
#     #body of finally block


# Raise :
# The keyword raise is used to throw an exception. For 
# example, we as a programmer can raise an exception if 
# certain condition happened. We have to define that what 
# kind of error to raise. 

# ex. of raise

# x = 5 
# if x == -5 :
#     print("this is -5")
# elif x == 5:
#     raise None("I don't like positive 5")
# else:
#     print("Every thing is ok")

# Output :-

# SyntaxWarning: 'NoneType' object is not callable; perhaps you missed a comma?
#   raise None("I don't like positive 5")
# Traceback (most recent call last):
#   File "c:\Users\iamle\OneDrive\Desktop\python practice\errorHandling\error.py", line 52, in <module>
#     raise None("I don't like positive 5")
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'NoneType' object is not callable

# one more ex. 

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# py", line 70, in <module>
    # raise TypeError("Only integers are allowed")
# TypeError: Only integers are allowed