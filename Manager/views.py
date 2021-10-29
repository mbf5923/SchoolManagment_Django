from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView

from Manager.middleware.policy import ManagerAccessToTeacherCheck, ManagerAccessToLessonCheck
from Manager.models import Lessons, Students
from Manager.transformers.user import UserResource, UserResourceCollection
from Manager.validators.TeacherValidator import ManagerNewTeacherValidation
from Manager.validators.LessonValidator import ManagerNewLessonValidation
from .transformers.student import StudentResource
from .validators.StudentValidator import ManagerNewStudentValidation, ManagerAssignLessonToStudentValidation

from School_Managment.middleware.auth import CustomAuthentication
from School_Managment.middleware.role import RoleCheck
from User.models import CustomUser
from .transformers.lesson import LessonResource,LessonResourceCollection



# Create your views here.
class ManagerNewTeacher(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def post(self, request):
        validator = ManagerNewTeacherValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        validator.data.update({
            'is_active_user': 1,
            'manager_id': request.user.id
        })
        user = self.model.objects.create(**validator.data)
        # add admin role for user
        user.roles_set.add(3)
        return Response(data=UserResource().setData(user))


class ManagerNewLesson(APIView):
    model = Lessons
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']), partial(ManagerAccessToTeacherCheck))

    def post(self, request):
        validator = ManagerNewLessonValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        validator.data.update({
            'manager_id': request.user.id
        })
        lesson = self.model.objects.create(**validator.data)
        return Response(data=LessonResource().setData(lesson))


class ManagerNewStudent(APIView):
    model = Students
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def post(self, request):
        validator = ManagerNewStudentValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        student = self.model.objects.create(**validator.data)
        return Response(data=StudentResource().setData(student))


class ManagerAssignLessonToStudent(APIView):
    model = Students
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']), ManagerAccessToLessonCheck)

    def post(self, request):
        validator = ManagerAssignLessonToStudentValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        try:
            student = self.model.objects.get(id=validator.data['student_id'])
        except self.model.DoesNotExist:
            return Response(status=404, data='student not found!')
        student.lesson.add(validator.data['lesson_id'])
        return Response(data=StudentResource().setData(student))


class ManagerListOfTeachers(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def get(self, request):
        teachers_list = self.model.objects.filter(manager_id=request.user.id)
        return Response(data=UserResourceCollection().setData(teachers_list))


class ManagerShowTeacher(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def get(self, request, teacher_id):
        try:
            teacher = self.model.objects.get(id=teacher_id, manager_id=request.user.id)
            return Response(data=UserResource().setData(teacher))
        except self.model.DoesNotExist:
            return Response(status=404, data='teacher not found!')


class ManagerListOfLessons(APIView):
    model = Lessons
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def get(self, request):
        lessons_list = self.model.objects.filter(manager_id=request.user.id)
        return Response(data=LessonResourceCollection().setData(lessons_list))


class ManagerShowLesson(APIView):
    model = Lessons
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def get(self, request, lesson_id):
        try:
            lesson = self.model.objects.get(id=lesson_id, manager_id=request.user.id)
            return Response(data=LessonResource().setData(lesson))
        except self.model.DoesNotExist:
            return Response(status=404, data='lesson not found!')