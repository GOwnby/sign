from django import forms

DESIGNATION = [
    ('Corporation','Corporation'),
    ('Branch','Branch'),
    ('Team','Team'),
    ('User','User')
]

class AccountForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.CharField(label='Email',  max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        limit = 12
        for index in range(int(extra_fields)):
            if index > limit:
                break
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = forms.CharField(label='Organization Type', widget=forms.Select(choices=DESIGNATION))