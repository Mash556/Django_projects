from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    teachers = models.ManyToManyField(
        'Teacher',
        related_name='students'
    )

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=40)
    expirience = models.IntegerField()
    students = models.ManyToManyField(
        Student,
        related_name='teachers'
        )


# from ManytoManyApp.models import Student, Teacher
# student1 = Student.objects.create(name='student1', age=2)
# student2 = Student.objects.create(name='student2', age=15)
# student3 = Student.objects.create(name='student3', age=20)
# student1.teacher.all()
# <QuerySet [<Teacher: Teacher object (1)>]>

# teacher1 = Teacher.objects.create(name='teacher1', subject='math', expirience=2)
# teacher1.students.set([student1, student2])
# обращаемся к связи и добавляем новых студентов
# teacher2 = Teacher.objects.create(name='teacher2', subject='bio', expirience=1)
# teacher2.students.set((student1, student3))
# teacher2.students.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>]>


# related_name | related_query_name