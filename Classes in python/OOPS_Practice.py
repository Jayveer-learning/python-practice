# Quiz one

# Write a Python program to create a Vehicle class with 
# max_speed and mileage instance attributes.

# class Vehical:

#     def __init__(self, max_speed, mileage):
#         self.myVehical_Max_speed = max_speed
#         self.myVehical_Mileage = mileage

#     def showVehicalInfo(self):
#         return f"my Vehical Max_speed is {self.myVehical_Max_speed} mileage is {self.myVehical_Mileage}"
# # instance/object of class Vehical 

# # instance/object 1
# myCar1 = Vehical("250km/hr", "5")
# print(myCar1.showVehicalInfo())

# # instance/object 2
# myCar2 = Vehical("390km/hr", "2")
# print(myCar2.showVehicalInfo())


# Quiz Two

# Create a child class Bus that will inherit 
# all of the variables and methods of the Vehicle class

# base/preant class
# class Vehical:

#     def __init__(self, max_speed, mileage):
#         self.myVehical_Max_speed = max_speed
#         self.myVehical_Mileage = mileage

# # child class
# class Bus(Vehical):

#     def __init__(self, max_speed, mileage, name):
#         self.my_Vehical_name_is = name
#         super().__init__(max_speed, mileage)

#     def ShowBusDataInfo(self):
#         return f"Bus name is {self.my_Vehical_name_is} Max_speed is {self.myVehical_Max_speed} mileage is {self.myVehical_Mileage}"
    
# # instance/object of class Vehical 

# # instance/object 1
# myBus1 = Bus("200km/hr", "5", "TaTa Bus")
# print(myBus1.ShowBusDataInfo())

# # instance/object 2
# myBus2 = Bus("390km/hr", "2","Volvo")
# print(myBus2.ShowBusDataInfo())

# interatance in OOP's
# class grandParent:
#     def __init__(self, gF_Name, gM_Name):
#         self.grandFather_Name = gF_Name
#         self.grandMother_Name = gM_Name
    
# class FatherSiblingName:
#     def __init__(self, Uncle1Name, Uncle2Name):
#         self.Uncle1Name_is = Uncle1Name
#         self.Uncle2Name_is = Uncle2Name

# class myParent:
#     def __init__(self, my_Father_Name_Is, my_Mother_Name_Is):
#         self.my_Father_Name_is = my_Father_Name_Is
#         self.my_Mother_Name_is = my_Mother_Name_Is
        

# class mySibling(myParent, FatherSiblingName, grandParent):
#     def __init__(self, gF_Name, gM_Name, my_Father_Name_Is, my_Mother_Name_Is, My_Name_is, my_Sister_Name_is_small_then_me, my_Small_siister, my_Most_Younget_brother_Name_Is, Uncle1Name, Uncle2Name, ):
#         self.My_Name_is = My_Name_is
#         self.my_Sister_Name_is_small_then_me = my_Sister_Name_is_small_then_me
#         self.my_Small_siister = my_Small_siister
#         self.my_Most_Younget_brother_Name_Is = my_Most_Younget_brother_Name_Is
#         grandParent.__init__(self, gF_Name, gM_Name)
#         FatherSiblingName.__init__(self, Uncle1Name, Uncle2Name)
#         myParent.__init__(self, my_Father_Name_Is, my_Mother_Name_Is)

#     def myFull_Family_Data(self):
#         return F"my Gf and gM name is {self.grandFather_Name} or {self.grandMother_Name} or my Parent Name {self.my_Father_Name_is} and {self.my_Mother_Name_is}, And My sibling Name is {self.my_Sister_Name_is_small_then_me} or {self.my_Small_siister} or brother is {self.my_Most_Younget_brother_Name_Is} and uncles Name is {self.Uncle1Name_is} and {self.Uncle2Name_is}"
    
# # instance/objetc of class mySibling;

# myFamilyData = mySibling("none", "none", "Mr's Jay singh", "Miss Aasha", "Jay veer", "Aaradhaya", "Garima", "Karishna", "none", "none")
# print(myFamilyData.myFull_Family_Data())


class favourate:
    def __init__(self, subject: list, DoingToLove: list ) -> None:
        self.subject = subject
        self.DoingToLove = DoingToLove

    def shopData(self) -> str:
        return f"favorate subject {self.subject} and Love to Doing {self.DoingToLove}"

# creating instance of class/favorate
fv_Thing = favourate(["physics", "chemisrty", "Maths"], ["programming", "Creating new things", "Thinking's"])
print(fv_Thing.shopData())


