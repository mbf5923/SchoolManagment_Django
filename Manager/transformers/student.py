from .lesson import LessonResourceCollection


class StudentResource:

    def setData(self, student):
        if student is None:
            return {}
        return {
            'id': student.id,
            'name': student.name,
            'family': student.family,
            'lessons': LessonResourceCollection().setData(student.lesson.all())
        }


class StudentResourceCollection:

    def setData(self, students):
        dict_data = []
        for item in students:
            user = StudentResource()
            dict_data.append(user.setData(item))
        return dict_data
