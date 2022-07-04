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



django=Course()
django.add_course(course_name="Django",status=True)
print(django.course_name)



djangob1=Batch()
djangob1.add_batch(course=django,batch_code="DjB1may2022",start_date="15-5-2022")
print(djangob1.batch_code)


ajith=Student()
ajith.add_student(student_name="Ajith MS",email="ajith@gmail.com",batch=djangob1)
print(ajith.student_name)
