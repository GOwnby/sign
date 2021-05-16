from django.shortcuts import render
from django.core import mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect

import json
import uuid
import datetime

import models
import forms


def index(request):
    return render(request, 'ManageDocument.html')

def uploaded(request):
    if request.method == 'POST':

        userID = request.COOKIES.get('user')

        numberOfDocumentDrafts = models.NumberOfDocumentDrafts.objects.get(pk=userID)
        numberOfDocumentDrafts.documents += 1
        numberOfDocumentDrafts.save()

        draftNonce = str(numberOfDocumentDrafts.documents)
        draftRequestID = userID + draftNonce
        form = forms.UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            handle_uploaded(request.FILES['docFile'], requestID)

            documents = models.Documents.objects.get(pk=userID)
            documents.documents += 1
            documents.save()
            documentNonce = str(documents.documents)
            requestID = userID + documentNonce

            documentID = uuid.uuid4()
            fingerprintCreated = uuid.uuid4()
            date = datetime.datetime.today()
            #exampleActionStamp = '2021=12-30:23;59+59[1234567890123456]_0'
            timestampCreated = (date.year + '=' + date.month + '-' + date.day + ':' + date.hour + ';' + date.minute 
                + '+' + date.second) + '[' + thisUser + ']' + '_0')

            document = models.Document(requestID = requestID, documentID = documentID, fingerprintCreated = fingerprintCreated,
                createdBy = userID, title = title, dateCreatedBy = timestampCreated)
            document.save()

            documentDraft = models.DocumentDrafts(userIDNonce=draftRequestID, documentKey=requestID)
            documentDraft.save()
            return HttpResponseRedirect('/UserDashboard/' + requestID)

    form = forms.UploadFileForm()

    return render(request, 'ManageDocument.html', {'form':form})


def handle_uploaded(docFile, requestID):
    with open('documents/' + requestID + '.pdf', 'wb+') as destination:
        for chunk in docFile.chunks():
            destination.write(chunk)


def ManageDocument(request, requestID):

    if request.method == 'POST':
        form = forms.AccessAccounts(request.POST)

        if form.is_valid:
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            permissions = form.cleaned_data['permissions']

            count = 1
            while True:
                try:
                    recieverUser = username[count]
                    recieverEmail = email[count]
                    recieverPermissions = permissions[count]
                    
                    userAddedToDocument(request, user, recieverUser, recieverEmail, recieverPermissions, requestID)
                    count += 1
                except Exception:
                    break


    document = models.Document.objects.get(pk=requestID)
    thisUser = request.COOKIES.get('user')
    writeAccess = False
    signAccess = False
    readAccess = False

    if (document.createdBy == thisUser):
        writeAccess = True
        signAccess = True
        readAccess = True
    else:
        associatedUsers = json.loads(document.associatedWith)
        if (associatedUsers['signer1'] == thisUser):
            signAccess = True
            readAccess = True

        if (associatedUsers['signer1'] != 'NoAdditionalSigners'):
            try:
                possibleUsers = 25
                count = 2
                while count <= possibleUsers:
                    if ( associatedUsers['signer' + str(count)] == thisUser ):
                        signAccess = True
                        readAccess = True
                        count += 1
            except Exception:
                print('Could not find Signer')

        if associatedUsers['cc1'] == thisUser:
        readAccess = True

        if (associatedUsers['cc1'] != 'NoAdditionalCC'):
            try:
                possibleUsers = 25
                count = 2
                while count <= possibleUsers:
                    if (associatedUsers['cc' + str(count)] == thisUser):
                        readAccess = True
                        count += 1
            except Exception:
                print('Could not find CC')
    access = [readAccess, signAccess, writeAccess]
    return render(request, 'ManageDocument.html', {'username':user,'access':access})

def CreatedDocument(request, title):
    documents = models.Documents.objects.get(pk=1)
    documents.documents += 1
    documents.save()

    documentNumber = str(documentNumber)
    thisUser = request.COOKIES.get('user')
    requestID = thisUser + documentNumber
    documentID = uuid.uuid4()
    fingerprintCreated = uuid.uuid4()
    date = datetime.datetime.today()
    #exampleActionStamp = '2021=12-30:23;59+59[1234567890123456]_0'
    timestampCreated = (date.year + '=' + date.month + '-' + date.day + ':' + date.hour + ';' + date.minute 
        + '+' + date.second) + '[' + thisUser + ']' + '_0')

    document = models.Document(requestID = requestID, documentID = documentID, fingerprintCreated = fingerprintCreated,
        createdBy = thisUser, title = title, dateCreatedBy = timestampCreated)
    document.save()

    ManageDocument(request, requestID)

def userAddedToDocument(request, sentFromUser, user, email, permissions, requestID):
    document = models.Document.objects.get(pk=documentID)

    numberOfDocumentsReceivedObj = models.NumberOfDocumentsReceived.objects.get(pk=user)
    numberOfDocumentsReceivedObj.documents += 1
    numberOfDocumentsReceivedObj.save()

    keyToKey = user + str(numberOfDocumentsReceivedObj.documents)
    documentReceived = models.DocumentsReceived(userIDNonce=keyToKey, documentKey=requestID)
    documentReceived.save()

    document.associatedWith[email] = perimssions
    document.save()

    if permissions = 'sign':
        subject = sentFromUser + 'has requested that you sign a document'
        text_content = user + ',\n\n' + sentFromUser + 'has requested that you sign the following document at IrisDocuments.com'
        html_content = render_to_string('templates/email/emailsigner.html')
    else:
        subject = sentFromUser + 'has requested that you view a document'
        text_content = user + ',\n\n' + sentFromUser + 'has requested that you view the following document at IrisDocuments.com'
        html_content = render_to_string('templates/email/emailcc.html')

    with mail.get_connection() as thisConnection:
        email = mail.EmailMultiAlternatives(subject, text_content, 'notify@alerts.irisdocuments.com', [email], connection=thisConnection)
        email.attach_alternative(html_content, 'text/html')
        email.send()