"""School_Managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import Index
from Auth import urls as auth_urls
from User import urls as user_urls
from Manager import urls as manager_urls
from Teacher import urls as teacher_urls

urlpatterns = [
    path('', Index.as_view()),
    path('auth/', include(auth_urls)),
    path('user/', include(user_urls)),
    path('manager/', include(manager_urls)),
    path('teacher/', include(teacher_urls)),
]
