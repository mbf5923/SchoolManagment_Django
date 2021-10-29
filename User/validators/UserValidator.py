from validator import Validator
from django.utils.translation import ugettext_lazy as _


class UserNewAdminValidation(Validator):
    phone = 'required|unique:AUTH_USER_MODEL,phone|regex:(9)[0-9]{9}'
    user_name = 'required|max_length:255'

    message = {
        'phone': {
            'required': _('phone is required'),
            'unique': _('phone is exist'),
            'regex': _('regx not true')
        },
        'user_name': {
            'required': _('user name is required'),
            'max_length': _('user name must smaller than 256 digits')
        }
    }
