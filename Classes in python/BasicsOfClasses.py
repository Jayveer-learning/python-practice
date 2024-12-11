# In programming, attributes means variables and behaviours means
#  functions .

# just take a ax. of car.

# attribute of car is -> color of car, size of car, model of
#  car, setting capacity of car they are attribute of car.

# behaviour of car is -> movement of a car, speed of a car,
# acceleration of a car, break of car, and steering steed of 
# a car these rae called function means behaviours.

# class Car:

#     # class attributes
#     typeOfCar = "Toyota"
#     def __init__(self, color):
#         # instance attributes    
#         self.car_color = color  #->Here we declare a variable
#         # self.car_color in which we save the value of the 
#         # attribute color .


# #  Almost everything in Python is an object with its 
# # properties and methods.

# # Objects are instances of classes. All objects follow the
# # specific class.

# #  We defined the class above named it as Car(). By defining 
# # it, means we only defined the description of object.   

# #? information :- NO memory or storage is allocated by just defining the class

#         car1 = Car("balck") # instance of class
#         car2 = Car("Red") # instance


# creating Multiple attributes class

# class Car:

#     def __init__(self, color, make, model, price): # color color, make, model is attribute
#         # the purpose of first parameter is to make individual
#         # copies of each instances so that the information do 
#         # not over write
        
#         self.car_color = color
#         self.car_make = make
#         self.car_model = model
#         self.car_price = price


#     #* Building functions within the classes
#     def description_of_car(self):
#         print(f"The starting price of {self.car_make} model{self.car_model} having color {self.car_color} price is {self.car_price}")


# It means each object of instance must have values for 
# these three attributes: color, make and model.


# The class Car() have three instances i-e Car 1 ,Car 2 and
# Car 3 . These instances are fulfilling the properties of a 
# class car . In the instance weprovide all the mandatory
# properties (in the initialization).

#Todo :- Car_1 is the unique indentifies for the particula 
# class car similarly Car_2 and Car# are also unique indentifier
# pointing to other cars.

# Instange is a copy of classes like Car_1 is first copy of 
# class, Like the instance Car_2, creates new copy of a class
# same as instance Car_3 create a new copy of class.

# and python matches the values of instance with the attribute/variable
# of the classe according to thier order. 

# Note that in each instance, there's a value that matches up 
# with the attribute, in the class definition above.

# callses and instance are like functions and we call the fucntion
# and then we put in inside function argument and the function
# mathched up with parameter in the function. same as class
# mathced up the instange value with class attribute/variable
# in according order.

#* creating a instanse are object of class Car

#! so we create instange out of the function and class scope 
# Car_1 = Car("Yellow", "Ford", "Mustang", "200k$")
# Car_2 = Car("Red", "Toyota", "Camry", "150k$")
# Car_3 = Car("Blue", "Honda", "Civic", "89k$")
# Car_4 = Car("White", "BMW", "M2", "500k$")

# Calling a function:- 

# syntax :- instance_name.function_name()

# Car_1.description_of_car() 
# #-> The starting price of Ford modelMustang having color Yellow price is 200k$

# Car_2.description_of_car()
# Car_3.description_of_car()
# Car_4.description_of_car()


#! Output :- 
# The starting price of Ford modelMustang having color Yellow price is 200k$
# The starting price of Toyota modelCamry having color Red price is 150k$
# The starting price of Honda modelCivic having color Blue price is 89k$
# The starting price of BMW modelM2 having color White price is 500k$





#* Need and clean Class 

# class Car:

#     def __init__(self, color, make, model, price):
#         self.car_color = color
#         self.car_make = make
#         self.car_model = model
#         self.car_price = price
    

#     #* Building functions within the classes
#     # The function will able to return full description of 
#     # that instance
#     def show(self):
#         print(f"The starting price of {self.car_make} model{self.car_model} having color {self.car_color} price is {self.car_price}")

# # instance/object of class Car
# Car_1 = Car("Yellow", "Ford", "Mustang", "200k$")
# Car_2 = Car("Red", "Toyota", "Camry", "150k$")
# Car_3 = Car("Blue", "Honda", "Civic", "89k$")
# Car_4 = Car("White", "BMW", "M2", "500k$")

# # Calling a function
# Car_1.show()
# Car_2.show()
# Car_3.show()
# Car_4.show()


# Output :-

# The starting price of Ford modelMustang having color Yellow price is 200k$
# The starting price of Toyota modelCamry having color Red price is 150k$
# The starting price of Honda modelCivic having color Blue price is 89k$
# The starting price of BMW modelM2 having color White price is 500k$


class Car:

    def __init__(self, color, make, model, price):
        self.car_color = color
        self.car_make = make
        self.car_model = model
        self.car_price = price

    # def show(self):
    #     print(f"The starting price of {self.car_make} model{self.car_model} having color {self.car_color} price is {self.car_price}")
    
# we have to write firsr parameter of class to each fucntion 
# within the class as follows,
# Syntax
# def Function_name(first_parameter_of_class):

    def budget(self):
        if self.car_price <= "200k$":
            print("Great! This car price is in your budget")
        else:
            print("This car is Too expensive")

Car_1 = Car("Yellow", "Ford", "Mustang", "200k$")
Car_4 = Car("White", "BMW", "M2", "500k$")

Car_1.budget() #--> Great! This car price is in your budget
Car_4.budget() #--> This car is Too expensive

# Output :-
# Great! This car price is in your budget
# This car is Too expensive
