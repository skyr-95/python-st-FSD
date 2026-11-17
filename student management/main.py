# class Student:
#     def __init__(self, usn, name, marks):
#         self.usn = usn
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("USN:", self.usn)
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#         print("------------------------")

# class student_management:
#     def __init__(self):
#         self.students = []

#     def add_student(self):
#         usn = input("Enter USN: ")

#         for existing_student in self.students:
#             if existing_student.usn == usn:
#                 print("Student with this USN already exists.")
#                 return

#         name = input("Enter student name: ")
#         marks = float(input("Enter marks: "))

#         new_student = Student(usn, name, marks)
#         self.students.append(new_student)
#         print("Student added successfully !.")

#     def view_students(self):
#         if not self.students:
#             print("No students found.")
#             return

#         for student in self.students:
#             student.display()

#     def search_student(self):

#         usn = input("Enter USN to search: ")
#         for student in self.students:
#             if student.usn == usn:
#                 print("Student found:")
#                 student.display()
#                 return
#         print("Student not found.")

#     def delete_student(self):    

#         usn = input("Enter USN to delete: ")
#         for student in self.students:
#             if student.usn == usn:
#                 self.students.remove(student)
#                 print("Student deleted")
# app = student_management()

# while True:
#     print("======== student management system ========")
#     print("1. Add student")
#     print("2. View students")
#     print("3. Search student")
#     print("4. Delete student")
#     print("5. Exit")

#     choice = input("Enter your choice : ")
#     if choice == "1":
#         app.add_student()
#     elif choice == "2": 
#         app.view_students() 
#     elif choice == "3":
#         app.search_student()
#     elif choice == "4":
#         app.delete_student()        
#     elif choice == "5":
#         print("thank you for using student management system")
#         break
#     else:
#         print("invalid choice. please try again.")