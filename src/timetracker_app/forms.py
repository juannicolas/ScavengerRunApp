from django import forms

from .models import RecordTime


class AddTimeForm(forms.ModelForm):
    class Meta:
        model = RecordTime
        fields = ['mpr_id', 'place_name_id']

    def clean_mpr_id(self):
        mpr_id = self.cleaned_data.get('mpr_id')
        if "MPR" not in mpr_id:
            return "MPR" + mpr_id
        return mpr_id
