from functools import partial

from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView
from Manager.models import Lessons, Students
# Create your views here.
from School_Managment.middleware.auth import CustomAuthentication
from School_Managment.middleware.role import RoleCheck
from Teacher.transformers.lesson import LessonResourceCollection, LessonResource
from Teacher.transformers.student import StudentResourceCollection, StudentResource


class TeacherLessonList(APIView):
    model = Lessons
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['teacher']),)

    def get(self, request):
        lessons = self.model.objects.filter(teacher_id=request.user.id)
        return Response(data=LessonResourceCollection().setData(lessons))


class TeacherShowLesson(APIView):
    model = Lessons
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['teacher']),)

    def get(self, request, lesson_id):
        try:
            lesson = self.model.objects.get(teacher_id=request.user.id, id=lesson_id)
            return Response(data=LessonResource().setData(lesson))
        except self.model.DoesNotExist:
            return Response(data='Lesson Not Found', status=404)


class TeacherStudentList(APIView):
    model = Students
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['teacher']),)

    def get(self, request):
        students = self.model.objects.filter(lesson__teacher=request.user.id).annotate(lesson_name=F('lesson__title'))
        return Response(data=StudentResourceCollection().setData(students))


class TeacherShowStudent(APIView):
    model = Students
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['teacher']),)

    def get(self, request, student_id):
        student = self.model.objects.filter(id=student_id, lesson__teacher=request.user.id).annotate(
            lesson_name=F('lesson__title')).first()
        if student:
            return Response(data=StudentResource().setData(student))

        return Response(data='student not found', status=404)
