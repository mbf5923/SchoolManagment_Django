from django.urls import path
from .views import *

urlpatterns = [
    path('lesson_list', TeacherLessonList.as_view()),
    path('show_lesson/<int:lesson_id>', TeacherShowLesson.as_view()),
    path('student_list', TeacherStudentList.as_view()),
    path('show_student/<int:student_id>', TeacherShowStudent.as_view()),
]
