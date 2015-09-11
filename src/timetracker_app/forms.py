from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import RecordTime


class AddTimeForm(forms.ModelForm):
    class Meta:
        model = RecordTime
        fields = ['mprid', 'place_name_id']

        widgets = {
            'mprid': forms.TextInput(attrs={'maxlength': '3',
                                            'class': 'form-control'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Ya existe un record en este Checkpoint para este ID"
            },
            'mprid': {
                'invalid_choice': "Ese ID no existe en record, favor de verificar y volver a intentar."
            }
        }
