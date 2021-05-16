from django.shortcuts import render
import math

from ManageDocument import models as DocumentModels
from ManageDocument import forms as DocumentForms
from CreateAccount  import models as AccountModels

class DocumentObject:
    def __init__(self, nonce, title, dateLastEdited, requestID):
        self.nonce = nonce
        self.title = title
        self.dateLastEdited = dateLastEdited
        self.requestID = requestID

def index(request):
    userID = request.COOKIES.get('user')
    form = forms.UploadFileForm()

    numberOfDocumentsSent = DocumentModels.Documents.objects.get(pk=userID).documents

    accountEmail = AccountModels.AccountLookup.objects.get(pk=userID).email
    account = AccountModels.Account.objects.get(pk=accountEmail)

    numberOfDocumentsReceived = account.documentsReceived
    numberOfActiveSent = account.activeSent
    numberOfActiveReceived = account.activeReceived

    return render(reuest, 'UserDashboard.html', {'form':form, 'documentsSent':numberOfDocumentsSent, 'documentsReceived':numberOfDocumentsReceived, 'activeSent':numberOfActiveSent, 'activeReceived':numberOfActiveReceived})

def completed(request, page):
    userID = request.COOKIES.get('user')

    accountEmail = AccountModels.AccountLookup.objects.get(pk=userID).email
    account = AccountModels.Account.objects.get(pk=accountEmail)

    numberOfDocumentsCompleted = DocumentModels.NumberOfDocumentsCompleted.objects.get(pk=userID).documents

    documents = []
    entries = page * 10
    entry_num = (numberOfDocumentsCompleted - entries)
    if entry_num <= 0:
        entry_num = 1
    while (entry_num < entry_num + 10):
        try:
            keyToKey = userID + str(entry_num)
            key = DocumentModels.DocumentsCompleted.objects.get(pk=keyToKey).documentKey
            documentModel = DocumentModels.Document.objects.get(pk=key)
            documentObject = DocumentObject(counter, documentModel.title, documentModel.dateLastEdited, key)
            documents.append(documentObject)
            entry_num += 1
        except Exception:
            break

    if (page == 1):
        if ((page + 2) * 10) < numberOfDocumentsCompleted:
            template_pages = [page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsCompleted:
            template_pages = [page, page+1]
        else:
            template_pages = [page]
    elif (page >= 2):
        if ((page + 2) * 10) < numberOfDocumentsCompleted:
            template_pages = [page-1, page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsCompleted:
            template_pages = [page-1, page, page+1]
        else:
            template_pages = [page-1, page]

    firstPageString = ''
    if (page >= 3):
        firstPageString = '1'
        
    lastPageString = ''
    if ((page + 3) * 10) < numberOfDocumentsCompleted:
        lastPageString = str( math.ceil(numberOfDocumentsCompleted / 10.0) )

    return render(request, 'UserDashboardTabView.html', {'page':template_pages,'documents':documents, 'firstpage':firstPageString, 'lastpage':lastPageString})

def sent(request, page):
    userID = request.COOKIES.get('user')

    accountEmail = AccountModels.AccountLookup.objects.get(pk=userID).email
    account = AccountModels.Account.objects.get(pk=accountEmail)

    numberOfDocumentsSent = DocumentModels.NumberOfDocumentsSent.objects.get(pk=userID).documents

    documents = []
    entries = page * 10
    entry_num = (numberOfDocumentsSent - entries)
    if entry_num <= 0:
        entry_num = 1
    while (entry_num < entry_num + 10):
        try:
            keyToKey = userID + str(entry_num)
            key = DocumentModels.DocumentsSent.objects.get(pk=keyToKey).documentKey
            documentModel = DocumentModels.Document.objects.get(pk=key)
            documentObject = DocumentObject(counter, documentModel.title, documentModel.dateLastEdited, key)
            documents.append(documentObject)
            entry_num += 1
        except Exception:
            break

    if (page == 1):
        if ((page + 2) * 10) < numberOfDocumentsSent:
            template_pages = [page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsSent:
            template_pages = [page, page+1]
        else:
            template_pages = [page]
    elif (page >= 2):
        if ((page + 2) * 10) < numberOfDocumentsSent:
            template_pages = [page-1, page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsSent:
            template_pages = [page-1, page, page+1]
        else:
            template_pages = [page-1, page]

    firstPageString = ''
    if (page >= 3):
        firstPageString = '1'
        
    lastPageString = ''
    if ((page + 3) * 10) < numberOfDocumentsSent:
        lastPageString = str( math.ceil(numberOfDocumentsSent / 10.0) )

    return render(request, 'UserDashboardTabView.html', {'page':template_pages,'documents':documents, 'firstpage':firstPageString, 'lastpage':lastPageString})


def drafts(request, page):
    userID = request.COOKIES.get('user')

    accountEmail = AccountModels.AccountLookup.objects.get(pk=userID).email
    account = AccountModels.Account.objects.get(pk=accountEmail)

    numberOfDocumentDrafts = DocumentModels.NumberOfDocumentDrafts.objects.get(pk=userID).documents

    documents = []
    entries = page * 10
    entry_num = (numberOfDocumentDrafts - entries)
    if entry_num <= 0:
        entry_num = 1
    while (entry_num < entry_num + 10):
        try:
            keyToKey = userID + str(entry_num)
            key = DocumentModels.DocumentDrafts.objects.get(pk=keyToKey).documentKey
            documentModel = DocumentModels.Document.objects.get(pk=key)
            documentObject = DocumentObject(counter, documentModel.title, documentModel.dateLastEdited, key)
            documents.append(documentObject)
            entry_num += 1
        except Exception:
            break

    if (page == 1):
        if ((page + 2) * 10) < numberOfDocumentDrafts:
            template_pages = [page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentDrafts:
            template_pages = [page, page+1]
        else:
            template_pages = [page]
    elif (page >= 2):
        if ((page + 2) * 10) < numberOfDocumentDrafts:
            template_pages = [page-1, page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentDrafts:
            template_pages = [page-1, page, page+1]
        else:
            template_pages = [page-1, page]

    firstPageString = ''
    if (page >= 3):
        firstPageString = '1'
        
    lastPageString = ''
    if ((page + 3) * 10) < numberOfDocumentDrafts:
        lastPageString = str( math.ceil(numberOfDocumentDrafts / 10.0) )

    return render(request, 'UserDashboardTabView.html', {'page':template_pages,'documents':documents, 'firstpage':firstPageString, 'lastpage':lastPageString})


def received(request, page):
    userID = request.COOKIES.get('user')

    accountEmail = AccountModels.AccountLookup.objects.get(pk=userID).email
    account = AccountModels.Account.objects.get(pk=accountEmail)

    numberOfDocumentsReceived = DocumentModels.NumberOfDocumentsReceived.objects.get(pk=userID).documents

    documents = []
    entries = page * 10
    entry_num = (numberOfDocumentsReceived - entries)
    if entry_num <= 0:
        entry_num = 1
    while (entry_num < entry_num + 10):
        try:
            keyToKey = userID + str(entry_num)
            key = DocumentModels.DocumentsReceived.objects.get(pk=keyToKey).documentKey
            documentModel = DocumentModels.Document.objects.get(pk=key)
            documentObject = DocumentObject(counter, documentModel.title, documentModel.dateLastEdited, key)
            documents.append(documentObject)
            entry_num += 1
        except Exception:
            break

    if (page == 1):
        if ((page + 2) * 10) < numberOfDocumentsReceived:
            template_pages = [page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsReceived:
            template_pages = [page, page+1]
        else:
            template_pages = [page]
    elif (page >= 2):
        if ((page + 2) * 10) < numberOfDocumentsReceived:
            template_pages = [page-1, page, page+1, page+2]
        elif ((page + 1) * 10) < numberOfDocumentsReceived:
            template_pages = [page-1, page, page+1]
        else:
            template_pages = [page-1, page]

    firstPageString = ''
    if (page >= 3):
        firstPageString = '1'
        
    lastPageString = ''
    if ((page + 3) * 10) < numberOfDocumentsReceived:
        lastPageString = str( math.ceil(numberOfDocumentsReceived / 10.0) )

    return render(request, 'UserDashboardTabView.html', {'page':template_pages,'documents':documents, 'firstpage':firstPageString, 'lastpage':lastPageString})
