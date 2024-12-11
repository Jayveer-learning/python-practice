# def fnArgs(*Name):
#     frdName = [Name]
#     return frdName

# MyFrinds = funArgs("js", "j. haimer", "me", "myTht", "myKnow.")
# print(MyFrinds)
# print(type(MyFrinds))


# name = "jayveer"

# if name == ":":
#     print("Lol wrong")
# elif name == "Jay":
#     print("Half")
# else:
#     print("Yes right but it's else block")

# for i in range(0, 10):
    # print(i)


#! Minimal line code

# a = int(input("Enter value for a "))
# b = int(input("Enter value for a "))
# result = "a is less than b" if(a<b) else"a is not less then b"
# print(result)


# print(type(myNewList))


# myNewList = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6]
# print(myNewList[0])
# print(len(myNewList))
# 
# myNewList.append(7)
# myNewList.pop()
# myNewList.insert(0, 0)
# myNewList.extend([11, 7, 10, 9, 8, 12])
# myNewList.sort()
# myNewList.reverse()
# myNewList.index(1)
# print(myNewList)
# 
# print(myNewList.count(1))
# myNewList = myNewList + [13, 14, 15, 16, 17]
# myNewList.sort(reverse=True) # --> reversed sorted value
# print(myNewList)
# 
# myNewList.remove(12)
# print(myNewList)
# myNewList.remove(13)
# print(myNewList)
# 
# myNewList.clear()
# print(myNewList)


# tuple()

# myTuple = ("delhi", "mumbai", "mumbai", "mumbai", "mumbai", "prayagraj", "kolkata", "harayana")
# print(myTuple[0:2])
# print(myTuple[-1])
# print(myTuple.count("mumbai"))

# myTupleToList = list(myTuple)
# print(myTupleToList)


# Dictionary in Python :-

# myDict = {"Name" : "JayVeer", "Class" : 11, "institute" : "HaimerDevHub"}
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())  
# # --> dict_items([('Name', 'JayVeer'), ('Class', 11), ('institute', 'HaimerDevHub')])
# square = {}
# for x in range(6):
#     square[x] = x*x
# print(square)  # --> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# print(myDict["Class"]) # --> 11
# print(myDict["institute"]) # --> HaimerDevHub
# print(len(myDict)) # --> 3

# myDict["Name"] = "J. Haimer"
# print(myDict) # --> {'Name': 'J. Haimer', 'Class': 11, 'institute': 'HaimerDevHub'}

# del(myDict["Class"])
# print(myDict) # --> {'Name': 'J. Haimer', 'institute': 'HaimerDevHub'}

# # Checking the key in the dictionary
# # syntax :- key in myDict

# print("Name" in myDict) # --> True
# print("Class" in myDict) # -- False

# # Checking the key in the dictionary using for loop and if .
# # 

# for item in myDict:
#     if "Name" in myDict:
#         print("Key Founds")
#         break
#     else:
#         print("No keys Founds")

# output :- Key Founds

# Accessing Keys of the dictionary

# for key in myDict.keys():
#     print(key)

# # Name
# # Class
# # institute

# # Accessing value

# for key in myDict.values():
#     print(key)
# JayVeer
# 11
# HaimerDevHub 

# Accessing pairs of dictionary

# for item in myDict.items():
#     print(type(item))  # --> return tuple value
# ('Name', 'JayVeer')
# ('Class', 11)
# ('institute', 'HaimerDevHub')

# Sorting the dictionary 

# information = {"john" : 59, "jerry" : 21, "Nohar" : 27, "Alex" : 51}
# for key, value in sorted(information.items()):
#     print(key, value)
# # Alex 51
# Nohar 27
# jerry 21
# john 59

# children =  dict()
# children["Name"] = ["Jayveer", "J. Haimer"]
# children["Age", "Class"] = [17, 11]
# print(children)
# {'Name': ['Jayveer', 'J. Haimer'], ('Age', 'Class'): [17, 11]}

# .3 Using set default() method 

#  In this method we iterate the list. In every iteration, we keep appending the
#  elements till given range.
#  We can do this by using setdefault()  method.
# dictionary = dict()

# List = [1, 2, 3]
# tupleData = ("a", "b", "c", "d")
# for value in List:
#     for element in range(int(value), int(value + 3)): #--> in range last value is not include
#         # that why we got [1, 2, 3] after [2, 3] like that. value is increment value. 
#         dictionary.setdefault(element, []).append(value)
# print(dictionary) #-> {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [2, 3], 5: [3]}



# Using list comprehension

# rangeValue = dict((val, range(int(val), int(val) + 2)) for val in [1, 2, 3])
# print(rangeValue)
# {1: range(1, 3), 2: range(2, 4), 3: range(3, 5)}



# function

# def body():
    # print("hello")
# body()
# print("Hello")



# Args *Parameter 

# def nameOfFriend(*friend):
#     print(f"Name of friends {friend}")

# nameOfFriend("rnsdfn", "asdlmflk", "sjsl", "jsjf", "nasfdn") # one parameter take mulsyiple argument help of Args. parameter
# output:-
# Name of friends ('rnsdfn', 'asdlmflk', 'sjsl', 'jsjf', 'nasfdn') 
#  -> Args *Parameter store argument in tuple data type and also return in tuple 

