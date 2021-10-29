from validator import Validator
from django.utils.translation import ugettext_lazy as _


class ManagerNewStudentValidation(Validator):
    name = 'required|max_length:255'
    family = 'required|max_length:255'

    message = {
        'name': {
            'required': _('name is required'),
            'max_length': _('name must smaller than 256 digits')
        },
        'family': {
            'required': _('family is required'),
            'max_length': _('family must smaller than 256 digits')
        }
    }


class ManagerAssignLessonToStudentValidation(Validator):
    lesson_id = 'required|numberic'
    student_id = 'required|numberic'

    message = {
        'lesson_id': {
            'required': _('lesson id is required'),
            'numberic': _('lesson id must be a number')
        },
        'student_id': {
            'required': _('student id is required'),
            'numberic': _('student id must be a number')
        }
    }
