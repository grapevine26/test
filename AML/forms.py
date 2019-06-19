from django import forms
from datetime import datetime

from .models import Client

year = datetime.today().year
YEARS = [x for x in range(1930, year)]


class ClientForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Client
        fields = (
            'analyst', 'first_name', 'last_name', 'government_id', 'phone_number', 'email', 'date_of_birth', 'address1',
            'address2', 'address_city', 'address_zip_code', 'address_country', 'country_of_citizenship',
            'company', 'company_field_of_business', 'company_state', 'company_country',
            'sns_facebook', 'sns_instagram', 'sns_twitter', 'sns_google',  'sns_linkedin'
        )

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for i in self.fields:

                self.fields[i].required = False
        # bootstrap class 추가
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})
        # placeholder 추가
        for i in self.fields:
            self.fields[i].widget.attrs.update({'placeholder': str(self.fields[i].label)})
