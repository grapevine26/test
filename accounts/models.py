from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    government_id = models.CharField(max_length=20, verbose_name='Government ID', )
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    date_of_birth = models.DateField(null=True, verbose_name='Date of Birth')
    address1 = models.CharField(max_length=100, verbose_name='Address 1')
    address2 = models.CharField(max_length=100, verbose_name='Address 2')
    address_city = models.CharField(max_length=100, verbose_name='City')
    address_zip_code = models.CharField(max_length=100, verbose_name='ZIP Code')
    address_country = CountryField(verbose_name='Country', blank_label='Country Select')
    country_of_citizenship = CountryField(verbose_name='Country of Citizenship', blank_label='Country of Citizenship Select')
    company = models.CharField(max_length=20, verbose_name='Company')
    company_field_of_business = models.CharField(max_length=20, verbose_name='Company Field of Business')
    company_state = models.CharField(max_length=20, verbose_name='State')
    company_country = CountryField(verbose_name='Country', blank_label='Country Select')
    sns_facebook = models.CharField(max_length=20, verbose_name='Facebook ID')
    sns_instagram = models.CharField(max_length=20, verbose_name='Instagram ID')
    sns_twitter = models.CharField(max_length=20, verbose_name='Twitter ID')
    sns_google = models.CharField(max_length=20, verbose_name='Google ID')
    sns_linkedin = models.CharField(max_length=20, verbose_name='Linkedin ID')
