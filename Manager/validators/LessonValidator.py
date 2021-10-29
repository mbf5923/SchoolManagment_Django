from validator import Validator
from django.utils.translation import ugettext_lazy as _


class ManagerNewLessonValidation(Validator):
    title = 'required|max_length:255'
    teacher_id = 'required|numberic'

    message = {
        'title': {
            'required': _('title is required'),
            'max_length': _('title must smaller than 256 digits')
        },
        'teacher_id': {
            'required': _('teacher id is required'),
            'numberic': _('teacher id must be a number')
        }
    }
