#for i in range (10):
 #   print("hello !! , good morning")

#def greet():
#    print("\n hello student")
 #   print("welcome to python programming\n")
#greet()

# def add(a,b):
#     result = a+b
#     print(result)
# add(10,20)
# add(50,30)


# students = ["pavan","amar","varsha","sheru"]
# print(students)
# students.append("nisha")
# print(students)
# students.remove("varsha")
# print(students)

# students_details = ("pavan", 20, 81, 0, True)
# print(students_details)


# student_info = {
#     "name": "pavan",
#     "age": 20,
#     "USN": 351,
#     "semester": 5,
#     "college": "GCEM",
#     "location": "Belagavi",
#     "passed": True,
    
# }
# # student_info["course"] = "python programming"
# # student_info["marks"] = 85
# print(
#     student_info["name"],
#     student_info["age"],
#     student_info["college"],
#     student_info["location"],
#     sep="\n",
# )


# class Student:
#     def display(self):
#         print("hello student")
#         print("welcome to python programming")

# s1 = Student()
# s1.display()        



# class Student:
#     def __init__(self, name, age, marks, ):
#         self.name = name
#         self.age = age
#         self.marks = marks
       

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

# s1 = Student("pavan", 20, 85.5)
# s2 = Student("amar", 21, 90.0)
# s1.display()
# s2.display()

# class student:
#     def __init__(self):
#         self.marks = 0

#     def input_marks(self, marks):
#         self.__marks = marks
#     def show_marks(self):
#         print("student marks:", self.__marks)

#         s1 = student()
#         s1.input_marks(85.5)
#         s1.show_marks()

# class grandfather:
#     def land(self):
#         print("grandfather has land")
# class father(grandfather):
#     def house (self):
#         print("father has house")
# class son(father):
#     def car(self):
#         print("son has car")
# class daughter(father):
#     def scooty(self):
#         print("daughter has scooty")

# s = son()
# s.land()    
# s.house()   
# s.car() 

# d = daughter()
# d.land()
# d.house()
# d.scooty()


# class animal:
#     def sound(self):
#         print("animal makes sound")

# class dog(animal):
#     def sound(self):
#         print("dog barks")

# class cat(animal):
#     def sound(self):
#         print("cat meows")

# animals = [dog(), cat(), animal()]
# for animal in animals:
#     animal.sound()


# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class upi(payment):
#     def pay(self, amount):
#         print(f"paid {amount} using UPI")

# class card(payment):
#     def pay(self, amount):
#         print(f"paid {amount} using credit card")

# p1 = upi()
# p2 = card()
# p1.pay(1000)
# p2.pay(2000)