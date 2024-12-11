# class Car:
#     def __init__(self, brand: str, feul_type: str) -> None:
#         self.brand_Of_Car = brand
#         self.feul_type_of_Car = feul_type

#     def drive(self, distance: float) -> None:
#         print(f"Driving {self.brand_Of_Car} for {distance}km [{self.feul_type_of_Car}]")
    
# # creating instance of Car class
# volvo : Car = Car("Volvo", "Diesel")
# bmw : Car = Car("Bmw", "Electric")

# print(volvo.drive(10))
# print(bmw.drive(150))



#* 1. Type Hints

# In your code, you see annotations like brand: str, feul_type: str, and distance: float. These are known as 
# type hints or type annotations. They provide a way to indicate the expected data type of the function parameters and 
# return values. Here’s what they mean:

#? Parameters:

#     brand: str: This indicates that the brand parameter is expected to be a string.
#     feul_type: str: This indicates that the feul_type parameter is also expected to be a string.
#     distance: float: This indicates that the distance parameter is expected to be a floating-point number.

#? end


def hello() -> None:
    print("Hello")

hello()
result = hello()
print(result) # --> return None becouse if we wrire function -> None that means function can't return any value only 
# print the value so if we store the function in another variable than we print the variable we got None becuse we 
# say that function can't return any thing.

# Contrast with Return Values
# if our function return value we can also specifie the return like that -> int , -> str, -> float, or -> bolean

def add(a, b) -> int:
    return a + b

print(add(4, 5))

def userName(user) -> str:
    return f"username is {user}"

print(userName("Jay veer"))

# like that we can make aur progam more readable and understandel code that way we use this and one thing i want to clear
# that this is can't make change on your code this is only for code understand and tell this function return this thing
# like -> None means this programm can't return any thing valuable and only print the value. that set.
