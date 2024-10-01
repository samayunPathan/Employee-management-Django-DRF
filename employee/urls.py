from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, AchievementViewSet, AchievementEmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'employee-achievements', AchievementEmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]