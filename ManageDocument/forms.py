from django import forms
from django_mysql.models import JSONField

class AccessAccounts(forms.Form):
    username = JSONField()
    email = JSONField()
    permissions = JSONField()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    docFile = forms.FileField()