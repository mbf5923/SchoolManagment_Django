class RoleResource:

    def setData(self, role):
        if role is None:
            return {}
        return {
            'id': role.id,
            'title': role.title
        }


class RoleResourceCollection:

    def setData(self, roles):
        dict_data = []
        for item in roles:
            role = RoleResource()
            dict_data.append(role.setData(item))
        return dict_data
