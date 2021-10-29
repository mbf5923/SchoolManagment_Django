from django.urls import path
from .views import *

urlpatterns = [
    path('new_admin', UserNewAdmin.as_view()),
    path('admin_list', UserAdminList.as_view()),
    path('new_manager', UserNewManager.as_view()),
    path('manager_list', UserManagerList.as_view()),
    path('new_teacher', UserNewTeacher.as_view())
]
