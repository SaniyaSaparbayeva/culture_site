from django import forms
from .models import *


# class RegistrationForm(forms.Form):
#     full_name = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     phone = forms.IntegerField()
#     birth_date = forms.DateField()
#     country = forms.CharField(max_length=200)
#     city = forms.CharField(max_length=200)
#     street_address = forms.CharField(widget=forms.TextInput(attrs={'cols':30, 'rows':10}))
#     postal_code = forms.CharField(max_length=10)


# class RegistrationForm(forms.Form):
#     class Meta:
#         model = RegistrationForm
#         fields = '__all__'



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        # fields = ['phone']
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs=
                                         {'class': "form-control",'pattern':'[A-Za-z ]{5,50}',
                                          'style': 'max-width: 300px;',
                                          'placeholder:': 'Name Surname'
                                          }),
            'email': forms.EmailInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',
                                          'placeholder:': 'Email'
                                          }),
            'phone': forms.TextInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',
                                          'placeholder:': 'Phone'
                                          }),
            'birth_date': forms.DateInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',
                                          'placeholder:': 'Birthdate'
                                          }),
            'country': forms.TextInput(attrs={'class': "form-control",'pattern': '[A-Za-z ]{5,50}',
                                          'style': 'max-width: 300px;',
                                          'placeholder:': 'Country'
                                          }),
            'city': forms.TextInput(attrs={'class': "form-control",'pattern': '[A-Za-z ]{5,50}',
                                          'style': 'max-width: 300px;',
                                          'placeholder:': 'City'
                                          }),
            'street_address': forms.TextInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',
                                          'placeholder:': 'Address'
                                          }),
            'postal_code': forms.TextInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',
                                          'placeholder:': 'ZIP Code'
                                          })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs=
                                         {'class': "form-control",'pattern':'[A-Za-z ]{2,50}',
                                          'style': 'max-width: 300px;',

                                          }),
            'surname': forms.TextInput(attrs=
                                    {'class': "form-control", 'pattern': '[A-Za-z ]{2,50}',
                                     'style': 'max-width: 300px;',

                                     }),
            'email': forms.EmailInput(attrs=
                                         {'class': "form-control",'style': 'max-width: 300px;',

                                          }),
            'message': forms.Textarea(attrs=
                                    {'class': "form-control"
                                     })

        }


class addPostForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs=
                                         {'class': "form-control",'pattern':'[A-Za-z ]{2,50}',
                                          'style': 'max-width: 300px;',

                                          }),
            'content': forms.Textarea(attrs=
                                    {'class': "form-control", 'pattern': '[A-Za-z ]{2,50}',
                                     'style': 'max-width: 300px;',

                                     }),
        }