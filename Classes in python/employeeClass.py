class employee:

    def __init__(self, name, age, gender, id_no, department):
        self.employee_name = name
        self.employee_age = age
        self.employee_gender = gender
        self.employee_id_no = id_no
        self.employee_department = department

    # employee Information function
    def employeeInfo(self):
        print(f"Name is {self.employee_name} age is {self.employee_age} and gneder {self.employee_gender} and id {self.employee_id_no} and department {self.employee_department}")

    # Role of Employee function
    def RoleOfEmployee(self):
        if self.employee_department == "AI and Ml Developer".lower():
            print(f"{self.employee_name} you are CEO of company")
        elif self.employee_department == "Senior Developer".lower():
            print(f"{self.employee_name} you are Team Leader")
        else:
            print(f"{self.employee_name} you are Developer")

# Instance/object of class employee
Employee_1 = employee("john", 28, "male", "25648", "web developer")
Employee_2 = employee("Leslie Burke", 19 ,"female", "792007", "senior developer")
Employee_3 = employee("J. haimer", 19, "male", "79200701", "ai and ml developer")

# calling function of RoleOfEmployee()
Employee_1.RoleOfEmployee()
Employee_2.RoleOfEmployee()
Employee_3.RoleOfEmployee()

Employee_1.employee_department
# output :- 
# john you are Developer
# Leslie Burke you are Team Leader
# J. haimer you are CEO of company
