from django.urls import path
from .views import *

urlpatterns = [
    path('send_otp', AuthSendOtp.as_view()),
    path('confirm_otp', AuthConfirmOtp.as_view()),
    path('check_token', AuthCheckToken.as_view())
]
