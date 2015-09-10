from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import RecordTime


class AddTimeForm(forms.ModelForm):
    class Meta:
        model = RecordTime
        fields = ['mpr_id', 'place_name_id']

        widgets = {
            'mpr_id': forms.TextInput(attrs={'maxlength': '3',
                                             'placeholder': 'MPR ID'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Ya existe un record en este Checkpoint para este ID"
            }
        }
