from rest_framework import serializers
from .models import Department, Achievement, Employee, AchievementEmployee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class AchievementEmployeeSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer(read_only=True)
    achievement_id = serializers.PrimaryKeyRelatedField(queryset=Achievement.objects.all(), write_only=True)

    class Meta:
        model = AchievementEmployee
        fields = ('id', 'achievement', 'achievement_id', 'achievement_date')

    def create(self, validated_data):
        achievement = validated_data.pop('achievement_id')
        return AchievementEmployee.objects.create(achievement=achievement, **validated_data)

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    achievements = AchievementEmployeeSerializer(source='achievementemployee_set', many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'phone', 'address', 'department', 'department_id', 'achievements')

    def create(self, validated_data):
        department = validated_data.pop('department_id')
        employee = Employee.objects.create(department=department, **validated_data)
        return employee

    def update(self, instance, validated_data):
        if 'department_id' in validated_data:
            department = validated_data.pop('department_id')
            instance.department = department
        return super().update(instance, validated_data)
