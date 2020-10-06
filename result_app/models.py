from django.db import models

# Create your models here.
class Subject(models.Model):
    Subject_Name = models.CharField(max_length=200)
    Subject_Code = models.CharField(max_length=200)
    Max_Marks = models.IntegerField()
    Course = models.CharField(max_length=200)
    Branch = models.CharField(max_length=100)
    Semester = models.IntegerField()

    def __str__(self):
        return self.Subject_Code

class Student(models.Model):
    studname = models.CharField(max_length=100)
    studroll = models.IntegerField(primary_key=True, editable=True)
    coursename = models.CharField(max_length=100)
    branchname = models.CharField(max_length=60)
    sem = models.IntegerField()
    mobile = models.CharField(max_length=100)
    adhar = models.CharField(max_length=100)
    gen = models.CharField(max_length=100)
    add = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    reg = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    session = models.CharField(max_length=100)

class Marks(models.Model):
    roll = models.IntegerField()
    subjectcode = models.CharField(max_length=20)
    subcode = models.ForeignKey(Subject,on_delete=models.CASCADE,default=2)
    marks = models.IntegerField()
    sheet = models.FileField(upload_to='marksheet')

    def get_subname(self):
        return self.subcode.Subject_Name

    def get_max_marks(self):
        return self.subcode.Max_Marks

    def get_sem(self):
        return self.subcode.Semester
