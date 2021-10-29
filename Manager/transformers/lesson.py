from .user import UserResource


class LessonResource:

    def setData(self, lesson):
        if lesson is None:
            return {}
        return {
            'id': lesson.id,
            'title': lesson.title,
            'manager': UserResource().setData(lesson.manager),
            'teacher': UserResource().setData(lesson.teacher),
        }


class LessonResourceCollection:

    def setData(self, lessons):
        dict_data = []
        for item in lessons:
            user = LessonResource()
            dict_data.append(user.setData(item))
        return dict_data
