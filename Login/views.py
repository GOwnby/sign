from django.shortcuts import render
from django.http import HttpResponseRedirect

import datetime

from . import forms
from . import ClientFunctions
import CreateAccount.models as models

def login(request):

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                userDB = models.Account.objects.get(pk=email)
            except BaseException:
                return HttpResponse('Account does not exist')
            else:
                if userDB.email == email:
                    if userDB.password == password:
                        response = HttpResponseRedirect('/UserDashboard/')
                        thisIP = ClientFunctions.get_client_ip(request)
                        userDB.currentIP = thisIP
                        CURRENT_TIME = datetime.datetime.today()
                        CURRENT_TIME = str(CURRENT_TIME.day) + '-' + str(CURRENT_TIME.month) + '=' + str(CURRENT_TIME.year)
                        userDB.lastLoginTime = CURRENT_TIME
                        userDB.save()
                        response.set_cookie('user', userDB.userID)
                        return response
    form = forms.LoginForm()
    
    return render(request, 'login.html', {'form':form})