from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms
from datetime import datetime

year = datetime.today().year
YEARS = [x for x in range(1930, year)]


class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = CustomUser
        fields = (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'government_id', 'phone_number',
            'date_of_birth', 'address1', 'address2', 'address_city', 'address_zip_code', 'address_country',
            'country_of_citizenship', 'company', 'company_field_of_business', 'company_state', 'company_country',
            'sns_facebook', 'sns_instagram', 'sns_twitter', 'sns_google', 'sns_linkedin'
        )
        labels = {
            'username': 'ID',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # help_text 안보이게
        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None
        # sns id 를 제외한 나머지는 필수입력
        for i in self.fields:
            if 'sns' in i:
                self.fields[i].required = False
            else:
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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
