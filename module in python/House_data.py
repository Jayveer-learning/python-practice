# creating a module 

class House:
    def __init__(self, price, country) -> None:
        self.price_of_House = price
        self.country = country

    def description(self):
        print(f"The average price of house located in {self.country} is {self.price_of_House}$")

House_One = House("$251,5146", "Us")
if __name__ == "__main__":
    House_One.description()

# so after this. this code run only 
# main file where create the instance of 
# class and call the the function 
