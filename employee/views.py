from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Employee, Department, Achievement, AchievementEmployee
from .serializers import EmployeeSerializer, DepartmentSerializer, AchievementSerializer, AchievementEmployeeSerializer

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]

class AchievementEmployeeViewSet(viewsets.ModelViewSet):
    queryset = AchievementEmployee.objects.all()
    serializer_class = AchievementEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
