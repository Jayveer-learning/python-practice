#  Reading and Writing in external file from Python code

# Perform this operation 
# Open the file
# Read or write in the file
# close the file

# we can also read and write file by using a 
# function with open()


# when we use with open so by closed automatically but if we 
# use only open need to close file manually like this 
# file_name.close

# syntax :- with open("file_name.txt", "mode") as file:

# file name :- The name of file we want to access or create
# mode :- python decide what he do with file like we have many
# thing like read, append, Write or more. mode we have

# The as in the syntax is a keyword returns a handler to the 
# file. Python needs a handle in order to get into the file. 
# In this case, I've given it a handle named file. The line 
# ends with the colon (:)

# todo :- WE can write any name instead of file like as data. 


# writing to text file 

with open("my_file.txt", "w") as file:
    file.write("This file write using python file method. ")

# reading file

with open("my_file.txt", "r") as read_data:
    file_data = read_data.read()
    print(file_data)

# todo: if the file doesn't exist then the read mode "r" will throw an error

# append data in file

with open("my_file.txt", "a") as file:
    file.write("this data written is append mode")

# read append file data using manuall open and close

with open("my_file.txt", "r") as file:
    read_A_data = file.read()
    print(read_A_data) # -> This file write using python file method. this data written is append mode

# but if i use write mode instead of append so old data replace
# by new data


# we have further modes:-

# w+
# r+
# a+

# w+ mode :-

# The w+ mode also allows us both to read the file as well as 
# write the data in the file.

# If the file not exists then w+ mode first create a file of 
# that name then writethe data to it.

# Here we just created a new file named it as new_file_1. 
# First the file willcreate and the text “In this mode we can read and read the text” added to
#  that file, works same as w mode.

with open("new_file_1.txt", "w+") as file:
    file.write("Tn this mode we can reaqd and write the text.")
    print(file.read()) # -> retunr an empty string


with open("new_file_2.txt", "w+") as file:
    file.write("Tn this mode we can reaqd and write the text.")
    file.seek(0)
    print(file.read()) # -> Tn this mode we can reaqd and write the text.
    # but why this return reason is seek() method

# So we use the method seek(). This method sets the current 
# position of the pointer at the offset. As we pass zero so it 
# sets to index zero. We can write as follows.


# todo :- Knowledge :- 
# we assume that the file should be in the same folder as the 
# python program taht opening it. But if the file is in the
# sub folders we have to giving the name of ther file

# We use backward slash in windows as followa,
# syntax :-

# with open("main_folder/file_name.txt", "mode") as file:

# we use a forward slash on Os X and linux as followa,

# with open("main_folder\file_name.txt", "mode") as file:


# r+ mode :-

# The r+ mode allows us both to read the file and write in the file.
# In mode works for the existing files.

# Remember :- Same as r mode if the file not exist then r+ mode
# will also show an error. 

with open("new_file_1.txt", "r+") as file:
    file.write("In this mode we can read and write the text ")
    file.write("But this will not create a file")
    file.seek(0) #-> current position of the pointer at zero index
    print(file.read()) # -> In this mode we can read and write the text But this will not create a file


#  Here we also use the method seek() to set the current 
# position of the pointer at zero index.


# todo :- Hint: 
# We can see the current position of cursor by using a method 
# tell(). this method return the current position in number of 
# bytes. we can use this method as follows,

with open("new_file_1.txt", "w+") as file:
    file.write("In this mode we can read and write the text. ")
    print(file.tell()) # -> 43 

    # its means that now the cursor position is at the last 
    # of ther following line.


# a+ mode 

# This mode opens a file for both appending and reading. 
# The file pointer is at the end of the file if the file 
# exists. The file opens in the append mode.


with open("new_file_1.txt", "a+") as file:
    file.write("This text is written in a+ mode.")
    file.seek(0)
    print(file.read()) # -> In this mode we can read and write the text. This text is written in a+ mode.

# In this mode, text is not over write but further added to 
# the file likeappending mode a

# todo :- Remember :- 
# if the file does not exits, it creates a new file for reading
# and writing.



# We have other modes in the following table. 

# modes       Description

# x       ->  Opens a file for exclusive creation. if the file
#             already exists then this mode create an error

# t       ->  Opens a file in text mode

# b       ->  Opens the file in binary mod

# rb      ->  Use for reading a binary file.

# rb+     ->  For reading or writing a binary file

# wb      ->  Opens a file for writing only in binary format.
#             Overwrites the file if the file exists.

# wb+     ->  For writing a binary file

# ab+     ->  Opens a file for both appending and reading in 
#             binary format.


# Task: Write a programme using all modes given in the above 
# table one by one. 
