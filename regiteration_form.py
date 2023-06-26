'''Students and Teacher regiteration form '''
question = input("You are a Teacher or Student")
lower_case = question.lower()
if lower_case == "teacher":
  
  name1 = input("Enter your name ")
  age1 = input("Enter your age ")
  salary1 = input("Enter your Salary ")
  Email1 = input("Enter your Email ")
  Phone1 = input("Enter Your Phone Number")

  class TeachersData:
    def __init__(self,name,age,salary,Email,Phone):
      self.name = name
      self.age = age
      self.salary = salary
      self.Email = Email
      self.Phone = Phone
    def showData(self):
      print("Teacher personal Information")
      print(f"Name:{self.name} \n Age: {self.age} \n Salary:       {self.salary}       \n Email: {self.Email} \n Phone: {self.Phone}")

  Teacher1 = TeachersData(name1,age1,salary1,Email1,Phone1)
  Teacher1.showData()
elif lower_case == "student":
  name1 = input("Enter your name ")
  age1 = input("Enter your age ")
  Class = input("Enter your Class ")
  Email1 = input("Enter your Email ")
  Phone1 = input("Enter Your Phone Number")

  class TeachersData:
    def __init__(self,name,age,Class,Email,Phone):
      self.name = name
      self.age = age
      self.Class = Class
      self.Email = Email
      self.Phone = Phone
    def showData(self):
      print("Teacher personal Information")
      print(f"Name:{self.name} \n Age: {self.age} \n Class:       {self.Class}       \n Email: {self.Email} \n Phone: {self.Phone}")

  Teacher1 = TeachersData(name1,age1,Class,Email1,Phone1)
  Teacher1.showData()
