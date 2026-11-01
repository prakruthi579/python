class Student:
    def __init__(self,id,name,department,python,java,sql,attendence):
        self.id=id
        self.name=name
        self.department=department
        self.python=python
        self.java=java
        self.sql=sql
        self.attendence=attendence
    def display(self):
        print(f"Id:{self.id}\nname:{self.name}\nDept:{self.department}\npython:{self.python}\njava:{self.java}\nsql:{self.sql}\natt:{self.attendence}")
        print(f"Total:{self.calculate_total()}\nPercentage:{self.calculate_percentage():.2f}\nGrade:{self.calculate_grade()}\nEligibility:{self.check_eligibility()}")
    def calculate_total(self):
        return self.python+self.java+self.sql  
    def calculate_percentage(self):
        return self.calculate_total()/3 
    def calculate_grade(self):
        percentage=self.calculate_percentage()
        if percentage>=85:
            return "A"
        elif percentage>=70:
            return "B"
        elif percentage>=55:
            return "c"
        elif percentage>=40:
            return "D"
        else:
            return "F"
    def check_eligibility(self):
        if self.attendence>=75 and self.calculate_percentage()>=40:
            return "Eligible"
        else:
            return "Not Eligible"
class StudentManager:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def display_all_students(self):
        if not self.students:
            print("no students available")
            return
        for student in self.students:
            student.display()
    def search_student(self,student_id):
        if not self.students:
            print("no students available")
            return
        for student in self.students:
            if student.id==student_id:
                student.display()
                break
        else:
            print("Student Not Found")
    def find_topper(self):
        if not self.students:
            print("no students available")
            return
        highest_percentage=None
        topper=None
        for student in self.students:
            percentage=student.calculate_percentage()
            if highest_percentage==None or percentage>highest_percentage:
                highest_percentage=percentage
                topper=student
        
        print("Topper iS:")
        topper.display()
    def calculate_class_average(self):
        if not self.students:
            print("No students available")
            return
        total=0
        for student in self.students:
            total+=student.calculate_percentage()
        return total/len(self.students)
    def students_by_grade(self,grade):
        if not self.students:
            print("no students available")
            return
        found=False
        for student in self.students:
            if student.calculate_grade()==grade.upper():
                student.display()
                found=True
        if not found:
            print("No student found with this grade")
    def count_grade(self):
        if not self.students:
            print("No students available")
            return
        grade_count={"A":0,"B":0,"C":0,"D":0,"F":0}
        for student in self.students:
            grade=student.calculate_grade()
            grade_count[grade]+=1
        for grade,count in grade_count.items():
            print(f"{grade} : {count}")
    def student_below_attendence(self,limit):
        if not self.students:
            print("No students available")
            return
        found=False
        for student in self.students:
            if student.attendence<limit:
                student.display()
                found=True
        if not found:
            print("No student found below this attendence")
    def update_marks(self,student_id,subject,new_marks):
        if not self.students:
          print("no students available")
          return
        subject=subject.lower()
        for student in self.students:
            if student.id==student_id:
                if subject=="python" :
                   
                   student.python=new_marks
                elif subject=="java":
                    student.java=new_marks
                elif subject=="sql":
                    student.sql=new_marks

                else:
                    print("Invalid subject")
                    return
                student.display()
                print("marks updated successfully")
                return
        
        print("Id not found")
    



            


                



student1=Student(101,"anu","ECE",85,78,90,92)
student2=Student(102,"ravi","EEE",90,93,95,98)
student3=Student(103,"priya","cse",80,70,75,68)
student1.display()
student2.display()
student3.display()
print(student1.calculate_total())
print(f"{student1.calculate_percentage():.2f}")
print(student1.calculate_grade())
print(student2.calculate_grade())
print(student1.check_eligibility())
print(student2.check_eligibility())
print(student3.check_eligibility())
manager=StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
manager.display_all_students()
empty_manager=StudentManager()
empty_manager.display_all_students()
student_id=int(input("enter the id to search: "))
manager.search_student(student_id)
empty_manager.search_student(student_id)
manager.find_topper()
empty_manager.find_topper()
print(manager.calculate_class_average())
empty_manager.calculate_class_average()
manager.students_by_grade("a")
manager.students_by_grade("B")
manager.students_by_grade("f")
empty_manager.students_by_grade("b")
manager.count_grade()
empty_manager.count_grade()
manager.student_below_attendence(75)
manager.student_below_attendence(60)
manager.student_below_attendence(100)
manager.update_marks(103,"python",90)
empty_manager.update_marks(105,"python",90)
manager.update_marks(104,"java",70)
manager.update_marks(102,"ec",80)
print("all features working good")


