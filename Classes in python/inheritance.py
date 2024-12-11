# Class Inheritance

# in Inheritance their are two type of classes

# -> Original Class :- The original or existing
# class is called base class. also parent class

# -> New Class :- The class which inherits
# the property of the base class is called
#  derived class or child class.

# We have following types of Inheritance

# -> Single Inheritance
# -> Multiple Inheritance
# -> multi level Inheritance
# -> Hierarchical Inheritance
# -> Hybrid Inheritance

# we wiil discuss each one by one

#! Single Inheritance
# Single Inheritance means that a derived class inherits the method and
# attributes from single base class.

# Syntax :-

# class Base_Class:
    
#     def __init__(self):
#         pass

# class Dervied_Class(Base_Class):

#     def __init__(self):
#         pass


# super class means base class and sub class means Dervied class
#* here We have super class Vehical and sub class Car().

# class Vehical:

#     def __init__(self, make, color):
#         self.car_make = make
#         self.car_color = color

#     def get_make(self):
#         return self.car_make
    
# class Car(Vehical):

#     def __init__(self, make, model, color):
#         # here, we call the constructor from the sub class Car
#         # using super().

#         # -> we call the attribute from super class by using 
#         # super(). Super() allows us to call a method from the
#         # base (super) class. We can also use name of the super
#         # class instead of super
#         # Vehical().__initi__(make, color)

#         super().__init__(make, color)
#         # instance attributes 
#         self.car_model = model

#     def get_description(self):
#         return f"the car is {self.car_color} and {self.car_make} {self.car_model}"

# # instance/obejct of class Car(Vehical)

# car_1 = Car("Ford", "Mustang", "Yellow")
# print(car_1.get_description())


# write a single Inheritance :

# Base class
# class Vehical:

#     def __init__(self, make, color):
#         self.car_make = make
#         self.car_color = color

#     # building funcition
#     def get_make(self):
#         return self.car_make
    
# # 
# class Car(Vehical):

#     def __init__(self, make, color, model):
#         # super() allow as to call method ofrom base (super) 
#         # class. we also use Base class name place of super()
#         super().__init__(make, color)
#         # instance attribute.
#         self.car_model = model

#     # function
#     def get_discription(self):
#         return f"The car is {self.car_make} and {self.car_color} {self.car_model}"
    

# Car_1 = Car("Ford", "yellow", "Mustang")
# print(Car_1.get_discription())
# output :-
# The car is Ford and yellow Mustang


#! Multiple Inheritance :-

# if any derived class unherits the property from multiple 
# base classes the it know as multiple inheritance.

# this method allow us use the properties from mutiple base classe
# in a derived or child class 

#?base Vehical class

# class Vehical:
#     def __init__(self, make):
#         self.car_make = make

#     def get_brand_name(self):
#         return self.car_make

#? Base Cost class
# class Cost:
#     def __init__(self, cost):
#         self.car_cost = cost
    
#     def get_cost(self):
#         return self.car_cost
    
# class Car(Vehical, Cost):

#     def __init__(self, make, model, cost):
#         self.car_model = model
#         Vehical.__init__(self, make)
#         Cost.__init__(self, cost)

#     def get_description(self):
#         return f"The stating price of {self.car_make} {self.car_model} is $ {self.car_cost}"
    
# # Instance/Object of class of Car using multiple Inheritance
# Car_1 = Car("Ford", "Mustang", "150K$")
# print(Car_1.get_description())
 
# Output:-
# The stating price of Ford Mustang is $ 150K$

#? practice 

# class Car:
#     def __init__(self, make, model, color):
#         self.car_make = make
#         self.car_model = model
#         self.car_color = color
    
#     def get_description(self):
#         return f"{self.car_color} color {self.car_make} {self.car_model}"

# car_1 = Car("ford", "mustang", "black")
# print(car_1.get_description()) # -> black color ford mustang


class Vehical:
    def __init__(self, model, color):
        self.car_color = color
        self.car_model = model
    
    def get_value(self):
        return f"{self.car_color} {self.car_model}"


class Car(Vehical):
    def __init__(self, model, color, make):
        self.car_make = make
        super().__init__(model, color)

    def get_data(self):
        return f"{self.car_color} {self.car_make} {self.car_color}"

car_1 = Car("Mustang", "yellow", "Ford")
print(car_1.get_data()) # --> yellow Ford yellow*



#! Multilevel Inheritance


# class Grandfather:
#     def __init__(self, grandfathername = None):
#         self.my_grandfathername = grandfathername

#     def grandfather(self):
#         return f"{self.my_grandfathername}"    

# class father(Grandfather):
#     def __init__(self, grandfathername, father= None):
#         self.my_father = father
#         super().__init__(grandfathername)

# class son(father):
#     def __init__(self, grandfathername, father=None):
#         super().__init__(grandfathername, father)

#     def parent_Inheritance(self):
#         print("my GrnadFather is {sel}")


class Company:
    def __init__(self, netWorth, netSell):
        self.total_netWorth = netWorth
        self.total_netSell = netSell
    
    def desplayCompanyData(self):
        return f"total company net wotrh us {self.total_netWorth} net sell {self.total_netSell}"

class WorkPartnerCompany(Company):
    def __init__(self, netWorth, netSell, profit):
        self.P_profit = profit
        # if we use super(). so we well can't use self inside init when we inheritanc the parent 
        # data
        # but when we use parent class name is neccessay use self inside init
        Company.__init__(self, netWorth, netSell) # Call Company constructor
    def showData(self):
        return f"total company net wotrh us {self.total_netWorth} net sell {self.total_netSell} and WP Profit {self.P_profit}"
#? Method Chaining: The super() function is used to call the parent class's constructor and reuse its logic.    

# instance/object of clsss Company and child WorkPartnerCompany(Company)
TotalDeta = WorkPartnerCompany("1B$", "10m", "200M$")
# WorkPartnerCompany(Company)
print(TotalDeta.showData())
# Company
print(TotalDeta.desplayCompanyData())
print(TotalDeta.total_netWorth) # -> accessing specific value.
# total company net wotrh us 1B$ net sell 10m and WP Profit 200M$
# total company net wotrh us 1B$ net sell 10m
