

class LessonResource:

    def setData(self, lesson):
        if lesson is None:
            return {}
        return {
            'id': lesson.id,
            'title': lesson.title,

        }


class LessonResourceCollection:

    def setData(self, lessons):
        dict_data = []
        for item in lessons:
            user = LessonResource()
            dict_data.append(user.setData(item))
        return dict_data
