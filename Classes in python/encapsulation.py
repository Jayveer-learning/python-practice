# Encapsulation :-

# As the word says, it encloses something in it like a capsule.
# When we make any sub class then it can easily accessy every
# attributes or method of super class. So if we want to keep it
# private? 

# for keeping then private we use the concept of encapsulation


# Knowledge:- Encapsulation gives us security and flexibility.
# It hides the data of a class from direct illegal access. 


# we will see how to make

# Private attributes 
# Private methods 

# to make a attribute private we use the underscore before the 
# variable name. 

# class Car:
#     def __init__(self, make: str, model: str) -> None:
#         self.car_make = make
#         self.car_model = model
#         self.__engine = "6.2L V-8"  # this is private attribute and default 
#         # instance attribute

#     def get_description(self) -> str:
#         return f"The car is {self.car_make} {self.car_model} {self.__engine}"

# # instacne/object of class
# car1: str = Car("Corvette", "Stingray")
# print(car1.car_make)
# print(car1.car_model)
# print(car1.__engine) # if we try to access private attribute 
# # give an error is 'Car' object has no attribute '__engine'

# # but we can acces private attribute use method
# print(car1.get_description()) # -> The car is Corvette Stingray 6.2L V-8


# making method private

# class Car_name:
#     def __init__(self, make: str, model: str) -> None:
#         self.car_make = make
#         self.car_model = model
#         self.__engine = "6.2L V-8"

#     def __engine_data(self) -> str:
#         return f"engine power is {self.__engine}"

#     def get_data(self) -> str:
#         return f"The car is {self.car_make} {self.car_model}"

# car2: str = Car_name("Corvette", "Stingray")
# print(car2.get_data()) #-> The car is Corvette Stingray
# print(car2.__engine_data())
# AttributeError: 'Car_name' object has no attribute '__engine_data'



# Accessing private members

# We can access private attribute and methods using esily
# look this example. 

# class Car:
#     def __init__(self):
#         self.car_make = "Corvette"
#         self.car_model = "Strigray"

#     def __engine(self) -> str:
#         return f"6.2L V-8"

#     def get_description(self) -> str:
#         return f"car name is {self.car_make} {self.car_model}"

# # instance/object of Car class 
# Car1 = Car()
# print(Car1.get_description())

# # accessing private attribute 
# print(f"Aceesing private variable: {Car1._Car__engine}")
# # Aceesing private variable: 6.2L V-8
# # syntax is :- 
# # instance_name._Car_name.__private_attribute_name

# # if we fallows this syntax we can access private attribute


# # Accessing private methods. 

# print(f"Accessing private Method: {Car1._Car__engine()}")
# Accessing private Method: 6.2L V-8

# Syntax :-
# instance_name._Car_name.__private_Method_name



# creating a encapsulation class

class Personal_information:
    def __init__(self) -> str:
        self.my_name: str = "Jay veer"
        self.Aka: str = "J. Haimer"
        self.__profession: str = "Programmer"
        self.__My_skill: list = ["Python developer", "Wev developer"]
        self.__My_crush: str = "Leslie Burke"

    def __show_Private_info(self) -> str:
        return f"{self.__profession} and skill {self.__My_skill} or crush {self.__My_crush}"

    def show_data(self) -> str:
        return f"my name is {self.my_name} {self.Aka}" 

# instance/object of class Personal_information 

Person = Personal_information()