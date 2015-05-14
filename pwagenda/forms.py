from django import forms
from pwagenda.models import Meeting
from django.contrib.auth.models import User
from pwagenda.models import Meeting, UserProfile
import datetime

class MeetingForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the meeting name.", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    emails = forms.EmailField(max_length=128, help_text="Email of participant", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    date = forms.DateField(initial=datetime.date.today, help_text="Type in day")
    time = forms.TimeField(initial=datetime.datetime.utcnow(), help_text="Type in time", widget=forms.TimeInput(format='%H:%M', attrs={'class':'form-control', 'size': '50'}), required=False)
    item = forms.CharField(max_length=128, help_text="First topic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}))
    subitem1 = forms.CharField(max_length=128, help_text="First subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    subitem2 = forms.CharField(max_length=128, help_text="Second subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    subitem3 = forms.CharField(max_length=128, help_text="Third subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    item1 = forms.CharField(max_length=128, help_text="First topic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    subitem4 = forms.CharField(max_length=128, help_text="First subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    subitem5 = forms.CharField(max_length=128, help_text="Second subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    subitem6 = forms.CharField(max_length=128, help_text="Third subtopic", widget=forms.TextInput(attrs={'class':'form-control', 'size': '50'}), required=False)
    item2 = forms.TextInput(attrs={'size':1130})

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Meeting
        fields = ('name', 'emails', 'date', 'time', 'item', 'subitem1', 'subitem2', 'subitem3', 'subitem4', 'subitem5', 'subitem6', 'item1', 'item2')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('company', 'picture')