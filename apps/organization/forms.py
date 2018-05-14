import re
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']


    def clean_mobile(self):
        """
        Check the mobile number is valid or not
        :return:
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^07[123]\d{7}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("Wrong mobile number format",code="Wrong format")
