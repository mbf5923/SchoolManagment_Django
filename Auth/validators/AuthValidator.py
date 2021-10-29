from validator import Validator
from django.utils.translation import ugettext_lazy as _


class PhoneValidation(Validator):
    phone = 'required|regex:(9)[0-9]{9}'

    message = {
        'phone': {
            'required': _('phone is required'),
            'regex': _('regx not true')
        }
    }


class OtpConfirmValidation(Validator):
    phone = 'required|regex:(9)[0-9]{9}'
    otp_code = 'required|numberic'

    message = {
        'phone': {
            'required': _('phone is required'),
            'regex': _('regx not true')
        },
        'otp_code': {
            'required': _('otp_code is required'),
            'numberic': _('otp_code must numberic'),
            'max_length': _('otp_code must 5 digits')
        }
    }
