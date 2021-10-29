from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView

from School_Managment.middleware.auth import CustomAuthentication
from School_Managment.middleware.role import RoleCheck

from User.models import CustomUser

# Create your views here.
from User.transformers.user import UserResource, UserResourceCollection
from User.validators.UserValidator import UserNewAdminValidation
from User.validators.TeacherValidator import UserNewTeacherValidation


class UserNewAdmin(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['admin']),)

    def post(self, request):
        validator = UserNewAdminValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        validator.data.update({
            'is_active_user': 1
        })
        user = self.model.objects.create(**validator.data)
        # add admin role for user
        user.roles_set.add(1)
        return Response(data=UserResource().setData(user))


class UserAdminList(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['admin']),)

    def get(self, request):
        admins = self.model.objects.filter(roles__code_name='admin')
        return Response(data=UserResourceCollection().setData(admins))


class UserNewManager(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['admin']),)

    def post(self, request):
        validator = UserNewAdminValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        validator.data.update({
            'is_active_user': 1
        })
        user = self.model.objects.create(**validator.data)
        # add admin role for user
        user.roles_set.add(2)
        return Response(data=UserResource().setData(user))


class UserManagerList(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['admin']),)

    def get(self, request):
        managers = self.model.objects.filter(roles__code_name='manager')
        return Response(data=UserResourceCollection().setData(managers))


class UserNewTeacher(APIView):
    model = CustomUser
    authentication_classes = [CustomAuthentication]
    permission_classes = (partial(RoleCheck, ['admin']),)

    def post(self, request):
        validator = UserNewTeacherValidation(request.data)
        status = validator.validate()
        if not status:
            return Response(status=422, data=validator.get_message())
        # check manager id has manager role
        target_manager = self.model.objects.filter(id=validator.data['manager_id'], roles__code_name='manager')
        if not target_manager:
            return Response(status=400, data='manager id is not true')
        validator.data.update({
            'is_active_user': 1
        })
        user = self.model.objects.create(**validator.data)
        # add admin role for user
        user.roles_set.add(3)
        return Response(data=UserResource().setData(user))
