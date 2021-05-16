from django.shortcuts import render

import datetime

from . import forms
from . import models as AccountModels
import Login.ClientFunctions as ClientFunctions
from ManageDocument import models as DocumentModels

def CreateAccount(request):

    if request.method == 'POST':
        form = forms.AccountForm(request.POST, extra=request.POST.get('extra_field_count'))

        if form.is_valid():
            form_username = form.cleaned_data['username']
            form_email = form.cleaned_data['email']
            form_password = form.cleaned_data['password']
            conf_pass = form.cleaned_data['confirm_password']
            if not(conf_pass == form_password):
                return HttpResponse('Passwords do not match')
            accounts = models.Accounts.objects.get(pk=1)
            accountNumber = accounts.users + 1
            accounts.save()

            accountNumber = str(accountNumber)
            lengthAccountNumber = len(accountNumber)
            if (lengthAccountNumber < 16):
                zeroes = 16 - lengthAccountNumber
                string = ''
                while zeroes != 0:
                    string = string + '0'
                    zeroes -= 1
                accountNumber = string + accountNumber

            thisIP = ClientFunctions.get_client_ip(request)
            CURRENT_TIME = datetime.datetime.today()                
            CURRENT_TIME = str(CURRENT_TIME.day) + '-' + str(CURRENT_TIME.month) + '=' + str(CURRENT_TIME.year)
            lastLoginTime = CURRENT_TIME
            newAccount = AccountModels.Account(userID = accountNumber, username = form_username, email = form_email, password = form_password, lastLoginTime = lastLoginTime, currentIP = thisIP)
            newAccount.save()
            newAccountLookup = AccountModels.AccountLookup(userID = accountNumber, email = form_email)
            newAccountLookup.save()
            
            initializeDocumentCount = DocumentModels.NumberOfDocumentsSent(userID =  accountNumber, documents = 0)
            initializeDocumentCount.save()
            initializeDocumentCount = DocumentModels.NumberOfDocumentsReceived(userID =  accountNumber, documents = 0)
            initializeDocumentCount.save()
            initializeDocumentCount = DocumentModels.NumberOfDocumentDrafts(userID =  accountNumber, documents = 0)
            initializeDocumentCount.save()
            initializeDocumentCount = DocumentModels.NumberOfDocumentsCompleted(userID =  accountNumber, documents = 0)
            initializeDocumentCount.save()
            initializeDocumentCount = DocumentModels.Documents(userID =  accountNumber, documents = 0)
            initializeDocumentCount.save()

            response = HttpResponseRedirect('/UserDashboard/')
            response.set_cookie('user', new_acc.userID)
            return response
        return HttpResponse('Bad Request')

    form = myForms.AccountForm()
    return render(request, 'createaccount.html', {'form':form})
