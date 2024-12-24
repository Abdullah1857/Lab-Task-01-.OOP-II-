#                 class and object
# class Hablu:
#     name=""
#     number=""
# a=Hablu()
# a.name="easam"
# print(a.name)

#                python inheritence

# class baba:
#     car="bmw"
#     tk="100 core"
#     home="10 floor"

# class kaka(baba):
#     BrokenPhone=""
#     BrokenHome=""

# k=kaka()
# print(k.car)

#                Multiple inheritence

# class baba:
#     car="bmw"
#     tk="100 core"
#     home="10 floor"

# class baba2:
#     smartphone="iphone"
#     AC="walton"
#     microphone="fifin"

# class baba3:
#     webcam="iphone"
#     laptop="walton"
#     camera="fifin"   

# class kaka(baba,baba2,baba3):
#     BrokenPhone=""
#     BrokenHome=""

# k=kaka()
# print(k.car)
# print(k.webcam)

#             multilevel inheritence

# class baba:
#     car="bmw"
#     tk="100 core"
#     home="10 floor"

# class son1(baba):
#     smartphone="iphone"
#     AC="walton"
#     microphone="fifin"

# class son2(son1):
#     webcam="iphone"
#     laptop="walton"
#     camera="fifin"   

# class son3(son2):
#     BrokenPhone="h"
#     BrokenHome="i"

# s=son3()
# print(s.car)
# print(s.webcam)
# print(s.BrokenHome)

#                      constructor

class parentinfo:
    def abdullahfamilly(self,name,age):  #method
        print(f"my name is{name},my age is {age}")
    def __init__(self,name,number):
        print(f"my name is{name},my number is {number}")


p1=parentinfo("abdullah","01816872153")
p1.abdullahfamilly("abdullah",23)

#                     polymorphism

# class vehicle:
#     def __init__(self,model,brand,component):
#         self.model=model
#         self.brand=brand
#         self.component=component

# class plane(vehicle):
#     pass

# class car(vehicle):
#     pass
# p1=plane("bm40","A","all components")
# c1=car("bmw024","bmw","main part")
# print(p1.brand)
# print(c1.model)

#                   encapsulation

# class parents:
#     def __init__(self,name,fathername):
#         self.__name=name
#         self.fathername=fathername
#         print(self.__name,self.fathername)
       

# class son1(parents): 
#     pass

# class son2(parents):
#     pass

# p1=parents("Ataur","Azizul")
# s1=son1("abdullah","Ataur")
# s2=son2("masud","Ataur")


#         exercise  polymorphism

# class Department:
#     def __init__(self,name):
#         self.name=name
#     def displayName(self):
#         print(f"Departmenr :{self.name}")

# class Teacher(Department):
#     def scheduleClass(self):
#         print("Class Time")
#     def gradeStudent(self):
#         print("student grade")
#     def displayName(self):
#         print("this is a teacher")

# class Author(Department):
#     def writeArticle(self):
#         print("write the artical")
#     def publishBlog(self):
#         print("This is a Author")

# class TeacherAuthor(Teacher,Author):
#     def __init__(self, name):
#         super().__init__(name)

# ta = TeacherAuthor("Computer Science")
# ta.displayName() 
# ta.scheduleClass()
# ta.gradeStudent()
# ta.writeArticle()
# ta.publishBlog()

#          exercise exception handling    ---Create a custom Exception and handle it in the following way:


# class InvaildException(Exception):
#     pass

# try:
#     age=int(input("Enter your age"))
#     if age<18:
#         raise InvaildException ("age is less then 18, Not6 eligable to vcote")
#     else:
#         print("Eligable for vote")

# except InvaildException as e:
#     print(e)



#            

# class SalaryNotInRange(Exception):
#     def __init__(self, salary):
#         super().__init__(f"Salary {salary} is not in the range of 10,000 to 50,000")


# class Rectangle:
#     def __init__(self, name, salary):
#         self.name = name
#         if not (10000 <= salary <= 50000):
#             raise SalaryNotInRange(salary)
#         self.salary = salary

#     def displaySalary(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")


# try:
#     emp = Rectangle("John", 60000)  # Will raise exception
#     emp.displaySalary()
# except SalaryNotInRange as e:
#     print(e)


#     Create a custom exception "insufficientFund" if balance is not greater than withdraw amount

#      ______________________
#      |                    |
#      |    BankAccount     |
#      |____________________|
#      |                    |
#      |+ balance           |
#      |____________________|
#      |                    |
#      |+ withdraw(amount)  |---> if amount > balance
#      |____________________|            then raise error
#                                 else print current ammount

# """

# class InsufficientFund(Exception):
#     def __init__(self, balance, withdraw_amount):
#         super().__init__(f"Insufficient funds: Balance {balance}, Withdraw Amount {withdraw_amount}")


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFund(self.balance, amount)
#         self.balance -= amount
#         print(f"Withdrawal successful. Current balance: {self.balance}")


# account = BankAccount(5000)

# try:
#     account.withdraw(6000)
# except InsufficientFund as e:
#     print(e)

# try:
#     account.withdraw(3000)
# except InsufficientFund as e:
#     print(e)


#                               Design the following code:

#      _____________________
#      |                   |
#      |      Vehicle      |
#      |___________________|
#      |                   |
#      |+ color            |
#      |___________________|
#      |                   |
#      |+ vehicleInfo()    |
#      |___________________|
#                ^
#                |
#      _____________________
#      |                   |
#      |       Taxi        |
#      |___________________|
#      |                   |
#      |-- model           |
#      |-- capacity        |
#      |-- variant         |
#      |___________________|
#      |                   |
#      |+ getModel()       |
#      |+ getCapacity()    |
#      |+ getVariant()     |
#      |+ setModel()       |
#      |+ setCapacity()    |
#      |+ setVariant()     |
#      |+ vehicleInfo()    |
#      |___________________|   -> Create two instances (t1, t2)

# """

# class Vehicle:
#     def __init__(self, color):
#         self.color = color

#     def vehicleInfo(self):
#         print(f"Vehicle Color: {self.color}")


# class Taxi(Vehicle):
#     def __init__(self, color, model, capacity, variant):
#         super().__init__(color)
#         self.__model = model
#         self.__capacity = capacity
#         self.__variant = variant

#     def getModel(self):
#         return self.__model

#     def getCapacity(self):
#         return self.__capacity

#     def getVariant(self):
#         return self.__variant

#     def setModel(self, model):
#         self.__model = model

#     def setCapacity(self, capacity):
#         self.__capacity = capacity

#     def setVariant(self, variant):
#         self.__variant = variant

#     def vehicleInfo(self):
#         super().vehicleInfo()
#         print(f"Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}")


# # Example usage
# t1 = Taxi("Yellow", "Toyota Prius", 4, "Hybrid")
# t2 = Taxi("White", "Honda Civic", 5, "Sedan")

# t1.vehicleInfo()
# t2.vehicleInfo()


# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def display(self):
#         return f"Name: {self.first_name} {self.last_name}"


# class Student(Person):
#     def __init__(self, first_name, last_name, graduation_year):
#         super().__init__(first_name, last_name)
#         self.graduation_year = graduation_year

#     def display(self):
#         return f"{super().display()}, Graduation Year: {self.graduation_year}"


# class Alumni(Student):
#     def __init__(self, first_name, last_name, graduation_year, passing_year):
#         super().__init__(first_name, last_name, graduation_year)
#         self.passing_year = passing_year

#     def display(self):
#         return f"{super().display()}, Passing Year: {self.passing_year}"


# class CurrentStudent(Student):
#     def __init__(self, first_name, last_name, graduation_year, current_semester):
#         super().__init__(first_name, last_name, graduation_year)
#         self.current_semester = current_semester

#     def display(self):
#         return f"{super().display()}, Current Semester: {self.current_semester}"


# class Employee(Person):
#     def __init__(self, first_name, last_name, emp_id):
#         super().__init__(first_name, last_name)
#         self.emp_id = emp_id

#     def display(self):
#         return f"{super().display()}, Employee ID: {self.emp_id}"


# class Teacher(Employee):
#     def __init__(self, first_name, last_name, emp_id, joining_year):
#         super().__init__(first_name, last_name, emp_id)
#         self.joining_year = joining_year

#     def display(self):
#         return f"{super().display()}, Joining Year: {self.joining_year}"


# class Admin(Employee):
#     def __init__(self, first_name, last_name, emp_id, joining_year):
#         super().__init__(first_name, last_name, emp_id)
#         self.joining_year = joining_year

#     def display(self):
#         return f"{super().display()}, Joining Year: {self.joining_year}"


# # Example Usage
# person = Person("John", "Doe")
# student = Student("Alice", "Smith", 2024)
# alumni = Alumni("Bob", "Brown", 2020, 2021)
# current_student = CurrentStudent("Cathy", "Davis", 2025, "6th")
# teacher = Teacher("David", "Evans", 1234, 2018)
# admin = Admin("Emily", "Clark", 5678, 2015)

# print(person.display())
# print(student.display())
# print(alumni.display())
# print(current_student.display())
# print(teacher.display())
# print(admin.display())

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def getName(self):
#         return self.name

#     def display(self):
#         print(f"Shape Name: {self.name}")


# class Rectangle(Shape):
#     def __init__(self, name, length, width):
#         super().__init__(name)
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

#     def display_Info(self):
#         print(f"Rectangle Name: {self.getName()}")
#         print(f"Length: {self.length}, Width: {self.width}")
#         print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")


# # Example usage
# rect = Rectangle("MyRectangle", 10, 5)
# rect.display_Info()

# class Employee:
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.emp_id = emp_id

#     def display_details(self):
#         return f"Employee Name: {self.name}, ID: {self.emp_id}"

# # Derived class for permanent employees
# class PermanentEmployee(Employee):
#     def __init__(self, name, emp_id, monthly_salary):
#         super().__init__(name, emp_id)
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary

# # Derived class for contract employees
# class ContractEmployee(Employee):
#     def __init__(self, name, emp_id, hourly_rate, hours_worked):
#         super().__init__(name, emp_id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked

# # Test data
# # Permanent Employee
# perm_emp = PermanentEmployee(name="Mr X", emp_id=4, monthly_salary=5000)
# print(perm_emp.display_details())
# print(f"Permanent Employee Monthly Salary: ${perm_emp.calculate_salary()}")

# # Contract Employee
# cont_emp = ContractEmployee(name="Mr Y", emp_id=3, hourly_rate=20, hours_worked=120)
# print(cont_emp.display_details())
# print(f"Contract Employee Salary: ${cont_emp.calculate_salary()}")







# import numpy as np

# # Sample sales data (rows: products, columns: months)
# sales_data = np.array([
#     [500, 600, 700, 800],  # Product 1 sales for months 1 to 4
#     [300, 400, 500, 600],  # Product 2 sales for months 1 to 4
#     [700, 800, 900, 1000], # Product 3 sales for months 1 to 4
#     [100, 150, 200, 250],  # Product 4 sales for months 1 to 4
#     [1200, 1300, 1400, 1500] # Product 5 sales for months 1 to 4
# ])

# # 1. Sales data for the first three products
# first_three_products = sales_data[:3, :]
# print("Sales data for the first three products:")
# print(first_three_products)

# # 2. Sales data for all products in the last two months (months 3 and 4)
# last_two_months_sales = sales_data[:, -2:]
# print("\nSales data for all products in the last two months:")
# print(last_two_months_sales)

# # 3. Sales data for the 2nd product in the 4th month
# specific_product_month_sales = sales_data[1, 3]
# print("\nSales data for the 2nd product in the 4th month:")
# print(specific_product_month_sales)