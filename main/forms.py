from django import forms
from django.core.mail import send_mail
from crega.settings import ENQUIRY_EMAIL


class EnquiryForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    company = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_mail('New enquiry received', self.cleaned_data['message'], self.cleaned_data['email'], [ENQUIRY_EMAIL], fail_silently=False)
