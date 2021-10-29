from django.urls import path
from .views import *

urlpatterns = [
    # ------------------- Teacher ------------------
    path('new_teacher', ManagerNewTeacher.as_view()),
    path('teacher_list', ManagerListOfTeachers.as_view()),
    path('teacher_show/<int:teacher_id>', ManagerShowTeacher.as_view()),
    # ------------------- Lesson ------------------
    path('new_lesson', ManagerNewLesson.as_view()),
    path('lesson_list', ManagerListOfLessons.as_view()),
    path('lesson_show/<int:lesson_id>', ManagerShowLesson.as_view()),
    # ------------------- Student ------------------
    path('new_student', ManagerNewStudent.as_view()),
    path('assign_lesson_to_student', ManagerAssignLessonToStudent.as_view())
]
