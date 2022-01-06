from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
#to enable access to views from other domains
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Import the models
from api_studrecman.models import CollegeSubject,StudentRecord,StudentSubjRec

# Import Serializer classes for the models
from api_studrecman.serializers import CollegeSubjectSerializer,StudentRecordSerializer,StudentSubjRecSerializer  


# Create your views here.

@csrf_exempt
def CollegeSubjectAPI(request, SubjectCode=""):
    if request.method=='GET':
         collegesubjects = CollegeSubject.all()
         collegesubjects_serializer=CollegeSubjectSerializer(collegesubjects,many=True)
         return JsonResponse(collegesubjects_serializer.data,safe=False)
    elif request.method=='POST':
        collegesubject_data=JSONParser().parse(request)
        collegesubjects_serializer=CollegeSubjectSerializer(collegesubject_data)
        if collegesubjects_serializer.is_valid():
            collegesubjects_serializer.save()
            return JsonResponse("A New College Subject has been added Successfully",safe=False)
        return JsonResponse("Could not Add the New College Subject", safe=False)
    elif request.method=='PUT':
        collegesubject_data=JSONParser().parse(request)
        collegesubject=CollegeSubject.objects.get(SubjectCode=collegesubject_data['SubjectCode'])
        collegesubjects_serializer=CollegeSubjectSerializer(collegesubject, collegesubject_data)
        if collegesubjects_serializer.is_valid():
            collegesubjects_serializer.save()
            return JsonResponse("Subject Record Update Completed Successfully")
        return JsonResponse("Could not update the Subject Record")
    elif request.method=='DELETE':
        collegesubject_data=JSONParser().parse(request)
        collegesubject=CollegeSubject.objects.get(SubjectCode=collegesubject_data['SubjectCode'])
        collegesubject.delete()
        return JsonResponse("College Subject Record Deleted",safe=False)
