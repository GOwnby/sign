from django.db import models
from django_mysql.models import JSONField

class DocumentsSent(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsSent(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0, max_length=32)

class DocumentDrafts(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentDrafts(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0, max_length=32)

class DocumentsReceived(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsReceived(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0, max_length=32)

class DocumentsCompleted(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    documentKey = models.CharField(max_length=32)

class NumberOfDocumentsCompleted(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.CharField(default=0, max_length=32)

class DocumentBlock(models.Model):
    userIDNonce = models.CharField(primary_key=True, max_length=32)
    blockAddress = models.IntegerField(max_length=32)

class Document(models.Model):
    requestID = models.CharField(primary_key=True, max_length=32)
    #documentID = models.CharField(max_length=32)
    createdBy = models.CharField(max_length=32)
    title = models.TextField(max_length=100)

    fingerprintCreated = models.CharField(max_length=32)
    fingerprintCompleted = models.CharField(max_length=32)
    fingerprintsPerAction = JSONField()

    # 0 = Draft 1 = Sent 2 = Completed
    documentProcess = models.IntegerField(max_length=2)

    dateCreatedBy = models.CharField(max_length=32)
    dateLastEdited = models.CharField(max_length=32)

    associatedWith = JSONField()

    timeAddedTo = JSONField()
    timeViewedBy = JSONField()
    timeSignedBy = JSONField()

    actionAtIPList = JSONField()

class Documents(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0, max_length=32)