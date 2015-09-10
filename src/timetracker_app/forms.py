from django import forms

from .models import RecordTime


class AddTimeForm(forms.ModelForm):
    class Meta:
        model = RecordTime
        fields = ['mpr_id', 'place_name_id']

        widgets = {
            'mpr_id': forms.TextInput(),
        }
