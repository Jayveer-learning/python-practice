import json # -> before using jason need to import json module

# Json stands for JavaScript Object Notation . As name says 
# that it is something related to JavaScript but python
# programmers can also use this.
# Recalling some concept from chapter 15, where we discussed 
# about writing the data in the text file as follows. 

listData = [1, 2, 3, 4, 5, 6, 7, 8]
jsonData = json.dumps(listData)
print(type(jsonData)) # -> <class 'str'> means json string
print(jsonData) # -> [1, 2, 3, 4, 5, 6, 7, 8]

jsonToList = json.loads(jsonData)
print(type(jsonToList)) # -> <class 'list'>
print(jsonToList) # -> [1, 2, 3, 4, 5, 6, 7, 8]

# Key Methods in json Module:

#1:- json.dumps(): Convert Python object to a JSON string.
#2:- json.loads(): Convert JSON string to a Python object.
#3:- json.dump(): Write JSON data to a file.
#4:- json.load(): Read JSON data from a file. 



#? Working with JSON in Python :-

# Python provides the json module to work with JSON data.
# 1. Converting Python objects to JSON (Serialization)

# You can convert Python data structures (like dictionaries, 
# lists, etc.) into JSON using the json.dumps() method.

data = {
    "name" : "john",
    "age" : 30,
    "is_student" : "True",
    "subject" : ["maths", "physics", "chemistry"],
    "address" : {
        "streert" : "123 main st", 
        "city" : "New York"
    }
}
print(type(data)) # -> <class 'dict'>

#? convert python object into JSON String using 
# json.dumps(nameofPyhton_Object, indent=4)

new_json_data = json.dumps(data, indent=4) # -> indent=4` makes 
# the output more readable give space we can write any thing 
# like no. it's optional but we write to make more readable
print(type(new_json_data))  # -> <class 'str'> it's json string
print(new_json_data) 
# ouput :-
# {
#     "name": "john",
#     "age": 30,
#     "is_student": "True",
#     "subject": [
#         "maths",
#         "physics",
#         "chemistry"
#     ],
#     "address": {
#         "streert": "123 main st",
#         "city": "New York"
#     }
# }


#? Converting JSON to Python objects (Deserialization)

# You can convert JSON data back into Python objects using 
# the json.loads() method.

jsonInto_python_Obj = json.loads(new_json_data)
print(type(jsonInto_python_Obj)) # -> <class 'dict'>



# Working with JSON files 

# when we working with file we use json.dump() or json.load()
# instance of json.dumps() json.loads()


# If you are working with a JSON file, you can use json.dump() 
# and json.load() to write and read data.


newdata = {
    "name" : "john",
    "age" : 30,
    "is_student" : "True",
    "subject" : ["maths", "physics", "chemistry"],
    "address" : {
        "streert" : "123 main st", 
        "city" : "New York"
    }
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)


# Reading JSON from a file:

with open("data.json", "r") as read_json_file:
    data = json.load(read_json_file)
    print(data)

# output :-

{'name': 'john', 'age': 30, 'is_student': 'True', 'subject': 
['maths', 'physics', 'chemistry'], 'address': 
{'streert': '123 main st', 'city': 'New York'}}


# now one json file create with name data.json. 
# so using file i/o we can create an json file. 


# Key Methods in json Module:

#     json.dumps(): Convert Python object to a JSON string.
#     json.loads(): Convert JSON string to a Python object.
#     json.dump(): Write JSON data to a file.
#     json.load(): Read JSON data from a file.


# Data Types Mapping

# JSON              ->        Python
# Object	        ->         dict
# Array	            ->         list
# String	        ->         str
# Number (int)      ->         int
# Number (float)    ->         float
# true/false	    ->         True/False
# null	            ->         None


