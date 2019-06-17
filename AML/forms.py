from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import ClientInformation
from django import forms
from datetime import datetime


class ClientInformationForm(forms.ModelForm):
    class Meta:
        model = ClientInformation
        fields = (
            'name', 'government_id', 'phone_number', 'date_of_birth', 'address1', 'address2', 'address_city',
            'address_zip_code', 'address_country', 'password', 'company', 'company_field_of_business', 'company_state',
            'company_country', 'sns_facebook', 'sns_instagram', 'sns_twitter', 'sns_google', 'sns_linkedin'
        )

    def __init__(self, *args, **kwargs):
        super(ClientInformationForm, self).__init__(*args, **kwargs)
        # help_text 안보이게
        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None
        # 필수입력
        for i in self.fields:
            self.fields[i].required = True
        # bootstrap class 추가
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})
        # placeholder 추가
        for i in self.fields:
            self.fields[i].widget.attrs.update({'placeholder': str(self.fields[i].label)})
        self.fields['username'].widget.attrs.update(
            {'title': self.fields['username'].help_text})
        self.fields['password1'].widget.attrs.update(
            {'title': "-password can't be too similar to your other personal information.\n" +
                      "-password must contain at least 8 characters.\n" +
                      "-password can't be a commonly used password.\n" +
                      "-password can't be entirely numeric."
             })
        self.fields['password2'].widget.attrs.update(
            {'title': self.fields['password2'].help_text})
