import sys
# sys module provide various variable and functions that used to manipulate the 
# different parts of the python runtime enverment.

# sys.version -> return the version of python interpreter with some extra information

print(sys.version) # -> 3.13.0 (tags/v



# input output

# stdin
# stdout
# stderr

#? stdin

# sys.stdin

# -> stdin: It can be used to get input from the command line directly. It is used 
# for standard input. It internally calls the input() method. It, also, automatically
# adds ‘\n’ after each

# for line in sys.stdin: 
# 	if 'q' == line.rstrip(): 
# 		break
# 	print(f'Input : {line}') 

# print("Exit") 



# for inputdata in sys.stdin:
    # print(inputdata)

#? stdout

# stdout: A built-in file object that is analogous to the interpreter’s standard output
# stream in Python. stdout is used to display output directly to the screen console. 
# Output can be of any form, it can be output from a print statement, an expression 
# statement, and even a prompt direct for input. By default, streams are in text mode. 
# In fact, wherever a print function is called within the code, it is first written 
# to sys.stdout and then finally on to the screen.


# sys.stdin -> is variable standard input

# sys.stdout -> work same as print but deffirent 
# sys.stdout -> show output that set. 

# sys.stdout.write("Hello world") #-> Hello world 
# print("\nhello") #-> hello 



#? stderr function in Python

# stderr: Whenever an exception occurs in Python it is written to sys.stderr.

def print_to_stderr(*a):
    print(*a, file= sys.stderr)

print_to_stderr("Hello world") #-> Hello world


# Command Line Arguments

print(sys.argv[0])
