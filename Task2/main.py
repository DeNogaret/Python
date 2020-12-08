from student import Student

print("Student info")

name = input("Input the name of the student: ")
student = Student(name)

student.set_gender(input("Input the gender: "))
student.set_age(int(input("Input the age: ")))
student.set_phone(input("Input the phone number: "))

print("Student created")

student.output()
