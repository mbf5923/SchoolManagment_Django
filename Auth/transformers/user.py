class UserResource:

    def setData(self, user):
        if user is None:
            return {}
        return {
            'id': user.id,
            'phone': user.phone,
            'user_name': user.user_name,
        }


class UserResourceCollection:

    def setData(self, users):
        dict_data = []
        for item in users:
            user = UserResource()
            dict_data.append(user.setData(item))
        return dict_data
