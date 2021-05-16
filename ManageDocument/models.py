from django.db import models

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
    #documentID = models.CharField(max_length=32)
    createdBy = models.CharField(max_length=32)
    title = models.TextField(max_length=100)

    fingerprintCreated = models.CharField(max_length=32)
    fingerprintCompleted = models.CharField(max_length=32)
    fingerprintsPerAction = models.JSONField()

    # 0 = Draft 1 = Sent 2 = Completed
    documentProcess = models.IntegerField()

    dateCreatedBy = models.CharField(max_length=32)
    dateLastEdited = models.CharField(max_length=32)

    associatedWith = models.JSONField()

    timeAddedTo = models.JSONField()
    timeViewedBy = models.JSONField()
    timeSignedBy = models.JSONField()

    actionAtIPList = models.JSONField()

class Documents(models.Model):
    userID = models.CharField(primary_key=True, max_length=16)
    documents = models.IntegerField(default=0)