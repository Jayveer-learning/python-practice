# write data using python in CSV Files

# CSV stand for commma separeted values. 

# It means that separator of each
# value is comma. We write comma after writing the first value
# then write the second value put a comma then write third 
# value and so on.

# importand : A CSV contains only text in it.

# CSV Files are basically simplified version of the spreadsheet
# or database.

# CVS Files like that  :- Each value separeted by comma


# Year, Club, Winner
# 2015, Barcelona, Lionel Messi
# 2016, Real Madrid, Cristiano Ronaldo
# 2017, Real Madrid, Cristiano Ronaldo
# 2018, Real Madrid, Loka Modric
# 2019, Barcelona, Lionel Messi


# hint :- As the value of each cell becomes comma separated 
# values and each row in spreadsheet becomes separate line in 
# CSV File. 

# we can do the following three things in csv file as we did 
# in text files

# read
# write
# append

# Reading the CSV files
# If a CSV file exists we can read the data from it easily. 

# Syntax: First we import csv, then open the file using 
# function with open(). Also, we have to assign a file handle
# i-e file . With the help of this file handle, python will 
# access the data of the CSV file. In line 3 we define a 
# variable which equals to the function csv.reader.

import csv # before using csv we need to import this then we
# csv file.

with open("file_name.csv", "w", newline="") as file:
    data_handel = csv.writer(file)
    data_handel.writerow(["Year", "Clud", "Winner"])
    data_handel.writerow(["2015", "Barcelona", "Lionel Messi"])
 
# with open("file_name.csv") as file:
#     readData = csv.reader(file)
#     print(readData)

#  Note that we pass the file handle file as an argument

# important: The data of the csv file returned by the function
# reader will not in the useable form. instence csv return the
# csv object like that <_csv.writer object at 0x00000202284FD180>

# we use this following syntax to make the data useable.
# we have thrre ways 

# first is this :- way merge data of csv that we got in multiple
# list we merge in one list 
with open("file_name.csv") as file:
    contents = csv.reader(file)
    competition = [] # -> create an empty list 
    for content in contents:
        competition += content
        print(competition) # -> ['Year', 'Clud', 'Winner', '2015', 'Barcelona', 'Lionel Messi']

# second way is this :-

with open("file_name.csv") as file:
    CVS_Data = csv.reader(file)

    for data in CVS_Data:
        print(data)

# Output :-
# ['Year', 'Clud', 'Winner']
# ['2015', 'Barcelona', 'Lionel Messi']        


# third way is this :- merge in one list but data separeted. 

with open("file_name.csv", "r") as file:
    data_Of_CVS = csv.reader(file)

    listOfCVS_Data = [] # -> create an empty list
    for dataFile in data_Of_CVS:
        listOfCVS_Data.append(dataFile)
        print(listOfCVS_Data)
# output :-
# [['Year', 'Clud', 'Winner'], ['2015', 'Barcelona', 'Lionel Messi']]

# TODO : When we don't give any parameter of mode(r,w) to the 
# CSV file by default it will read that file.



# with open("file_name1.csv", "w", newline="") as file:
#     data_handel = csv.writer(file)
#     data_handel.writerow(["2015", "Barcelona", "Lionel Messi"])

# # create same thing again for more understanding
# with open("file_name1.csv") as file:
#     contents = csv.reader(file)
#     competition = [] # -> create an empty list 
#     for content in contents:
#         competition += content
# print(competition)

# club = input("Enter the name of a club: ")
# index_number_of_club = competition.index(club) # -> index give
# #  index no. of club input value if exist
# index_number_of_winner = index_number_of_club + 1
# Winner = competition[index_number_of_winner]
# print(f"The Winner of club {club} is {Winner}")
# output :- The Winner of club Barcelona is Lionel Messi


# we can also do using year and + 2 




#? Writing in the CSV files

# We can load data to any csv file by defining the name of that csv file.

# Syntax:

# The syntax is almost same as for reading a CSV file. 
# Just we pass parameter w (in quotation marks) for writing 
# data in it. Also we have to define a file handle. We call 
# the function writer in the csv module.

# The parameter newline (used in the syntax) having the value 
# None by default. It generates empty line between two rows. 
# We can remove that line newline = “”

# For technical reasons, we can't write data directly to the 
# CSV file. So we defined a variable, and give any legal name 
# to it. Then, the variable connected by a dot to the keyword
# writerow . Each row is loaded into the handler as a list.

print() # -> for space in output panel
print()
print() 


with open("nameOf_file.csv", "w", newline="") as file:
    data_handel = csv.writer(file)

    data_handel.writerow(["Year", "champion", "top score"])
    data_handel.writerow(["Year1", "champion1", "top score1"])
    data_handel.writerow(["Year1", "champion1", "top score1"])
    data_handel.writerow(["Year1", "champion1", "top score1"])


# todo :- If we one time import cvs in the code file we don't
# need to import again.


#? Appending to CSV files :
# We can append more data to existing file without removing the previous
# data

# todo :- We can add more data to the existing CSV file in the
# form of lists. 

# same as write only change the mode "a" then csv file in append
# mode if after we add data using "a" mode if we add data then 
# data append in csv file. 

with open("nameOf_file.csv", "a", newline="") as file:
    data_handel = csv.writer(file)

    data_handel.writerow(["Year", "champion", "top score"])
    data_handel.writerow(["Year1", "champion1", "top score1"])
    data_handel.writerow(["Year1", "champion1", "top score1"])
    data_handel.writerow(["Year1", "champion1", "top score1"])


with open("nameOf_file.csv") as file:
    read_Data = csv.reader(file)

    for data in read_Data:
        print(data)

# Output :-
# ['Year', 'champion', 'top score']
# ['Year1', 'champion1', 'top score1']
# ['Year1', 'champion1', 'top score1']
# ['Year1', 'champion1', 'top score1']
# ['Year', 'champion', 'top score']
# ['Year1', 'champion1', 'top score1']
# ['Year1', 'champion1', 'top score1']
# ['Year1', 'champion1', 'top score1']

