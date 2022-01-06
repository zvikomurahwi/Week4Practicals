from dyango.conf.urls import urls
from api_studrecman import views
from views import CollegeSubjectAPI

urlpatterns = [
    url(r'^subjectcode$',views.CollegeSubjectAPI)
    url(r'^subjectcode/$', views.CollegeSubjectAPI)
]
