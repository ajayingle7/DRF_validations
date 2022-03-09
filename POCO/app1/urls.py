from django.urls import path
from .views import EmployeeDetail,EmpInfo



urlpatterns = [
    path("emp/", EmployeeDetail.as_view()),
    path("emp/<int:id>/", EmpInfo.as_view())



]