from rest_framework import permissions


class RoleCheck(permissions.BasePermission):
    message = 'Access Deny!'

    def __init__(self, allowed_roles):
        super().__init__()
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        current_user = request.user
        #print(current_user.roles_set.filter(code_name__in=self.allowed_roles).query)
        return current_user.roles_set.filter(code_name__in=self.allowed_roles).exists()
