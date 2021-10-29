from rest_framework import permissions

from User.models import CustomUser
from Manager.models import Lessons


class ManagerAccessToTeacherCheck(permissions.BasePermission):
    message = 'Access Deny!'

    def __init__(self):
        super().__init__()

    def has_permission(self, request, view):
        current_user = request.user
        if 'teacher_id' not in request.data:
            return False
        return CustomUser.objects.filter(id=request.data['teacher_id'], manager_id=current_user.id)


class ManagerAccessToLessonCheck(permissions.BasePermission):
    message = 'Access Deny!'

    def __init__(self):
        super().__init__()

    def has_permission(self, request, view):
        current_user = request.user
        if 'lesson_id' not in request.data:
            return False
        return Lessons.objects.filter(id=request.data['lesson_id'], manager_id=current_user.id)
