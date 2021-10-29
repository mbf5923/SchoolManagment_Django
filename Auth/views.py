import hashlib
import random
from datetime import datetime
from functools import partial

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from Auth.transformers.user import UserResource
from Auth.validators.AuthValidator import PhoneValidation, OtpConfirmValidation
from School_Managment.middleware.auth import CustomAuthentication
from School_Managment.middleware.role import RoleCheck
from User.models import CustomUser


# Create your views here.


class AuthSendOtp(APIView):
    model = CustomUser

    def post(self, request):
        validator = PhoneValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())

        phone = request.data['phone']
        if cache.get('otp_' + str(phone), ):
            return Response(status=400, data='too early request')
        # check not exist before
        user = self.model.objects.filter(phone=request.data['phone']).first()
        if not user:
            user = self.model.objects.create(phone=phone)
        user = UserResource().setData(user)
        otp = random.randint(10000, 99999)
        cache.set('otp_' + str(phone), otp, timeout=120)
        new_dict = {'otp': otp}
        user.update(new_dict)
        return Response(data=user)


class AuthConfirmOtp(APIView):
    model = CustomUser

    def post(self, request):
        validator = OtpConfirmValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())

        phone = request.data['phone']
        cached_otp = cache.get('otp_' + str(phone), )
        if not cached_otp:
            return Response(data='not otp found', status=401)
        if cached_otp == request.data['otp_code']:
            cache.delete('otp_code')
            to_hash = datetime.now().timestamp()
            to_hash = str(to_hash) + str(phone) + str(cached_otp)
            api_token = hashlib.md5(to_hash.encode()).hexdigest()
            CustomUser.objects.filter(phone=phone).update(api_token=api_token)
            return Response(data={'token': api_token})
        return Response(data='otp not true', status=401)


class AuthCheckToken(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['manager']),)

    def get(self, request, **kwargs):
        return Response(data=UserResource().setData(request.user))

