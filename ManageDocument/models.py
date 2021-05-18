from django.db import models
import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'documents/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class DocumentsSent(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsSent(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)

class DocumentDrafts(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentDrafts(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)

class DocumentsReceived(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsReceived(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)

class DocumentsCompleted(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsCompleted(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)

class DocumentBlock(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    blockAddress = models.IntegerField()

class Document(models.Model):
    requestID = models.CharField(primary_key=True, max_length=32)
    createdBy = models.CharField(max_length=32)
    title = models.TextField(max_length=100)
    document = models.FileField(upload_to=path_and_rename)

    fingerprintCreated = models.CharField(max_length=64)
    fingerprintCompleted = models.CharField(max_length=64)



#    documentID = models.CharField(max_length=32)

#    dateCreatedBy = models.CharField(max_length=32)
#    dateLastEdited = models.CharField(max_length=32)
#    fingerprintsPerAction = models.JSONField()

#    0 = Draft 1 = Sent 2 = Completed
#    documentProcess = models.IntegerField()



#    associatedWith = models.JSONField()

#    timeAddedTo = models.JSONField()
#    timeViewedBy = models.JSONField()
#    timeSignedBy = models.JSONField()

#    actionAtIPList = models.JSONField()

class Documents(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)