from rest_framework import serializers
from api_studrecman.models import CollegeSubject,StudentRecord,StudentSubjectRec

class CollegeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollegeSubject
        fields=('SubjectCode','SubjectName')

class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRecord
        fields=('StudentId','Firstname','Surname','MeanMarks','StudGrade')

class StudentSubjectRecSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentSubjectRec
        fields=('StudentSubjRecId','StudentId','SubjectCode','SubjectScore')