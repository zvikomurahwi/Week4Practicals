from django.db import models

# Create your models here.

class CollegeSubject(models.Model):
    SubjectCode = models.CharField(max_length=20, primary_key=True)
    SubjectName = models.CharField(max_length=50)

class StudentRecord(models.Model):
    StudentId = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    MeanMarks = models.DecimalField(max_digits=5,decimal_places=2)
    StudGrade = models.CharField(max_length=4)

class StudentSubjectRec(models.Model):
    StudentSubjRecId = models.AutoField(primary_key=True)
    StudentId = models.IntegerField(default = 1)
    SubjectCode = models.CharField(max_length=20)
    SubjectScore = models.IntegerField()

