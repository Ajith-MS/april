class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name


dj=Course()
dj.add_course(course_name="Django",status=True)
ms=Course()
ms.add_course(course_name="Meanstack",status=True)
bd=Course()
bd.add_course(course_name="Bigdata",status=True)
print(dj)

djb1=Batch()
djb1.add_batch(course=dj,batch_code="djmay2022",start_date="11-5-2022")

msb1=Batch()
msb1.add_batch(course=ms,batch_code="msmay2022",start_date="15-5-2022")

print(djb1)
print(djb1.course)
print(djb1.course.status)

vishnu=Student()
vishnu.add_student(student_name="Vishnu",email="vishnu@gmail.com",batch=djb1)

ajith=Student()
ajith.add_student(student_name="ajith",email="ajith@gmail.com",batch=djb1)
print(vishnu)
print(ajith)

deego=Student()
deego.add_student(student_name="Deego",email="deego@gmail.com",batch=msb1)
abhay=Student()
abhay.add_student(student_name="Abhay",email="abhay@gmail.com",batch=msb1)
print(deego)

students=[]

students.append(vishnu)
students.append(ajith)
students.append(deego)

# for student in students:
#     print(student)

ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="Meanstack"]
print(ms_stud)