from django.db import models
from django.db.models import JSONField

class Accounts(models.Model):
    key = models.IntegerField(primary_key=True, default=1)
    users = models.IntegerField(default=0)

class Account(models.Model):
    userID = models.CharField(max_length=16)
    username = models.CharField(max_length=100)
    email = models.CharField(primary_key=True, max_length=128)
    password = models.CharField(max_length=100)
    lastLoginTime = models.CharField(max_length=16)
    currentIP = models.CharField(max_length=32)
    signature1 = models.ImageField()
    signature2 = models.ImageField()
    signature3 = models.ImageField()

    activeSent = models.IntegerField()
    activeReceived = models.IntegerField()

    receivedDocumentIDs = models.JSONField()
    documentsReceived = models.IntegerField()

class AccountLookup(models.Model):
    userID = models.CharField(max_length=32, primary_key=True)
    email = models.CharField(max_length=128)

class Corporation(models.Model):
    userOwnerEmail = models.CharField(primary_key=True, max_length=128)
    branchesAssociated = models.JSONField()

class Branch(models.Model):
    userOwnerEmail = models.CharField(primary_key=True, max_length=128)
    teamsAssociated = models.JSONField()

class Team(models.Model):
    userOwnerEmail = models.CharField(primary_key=True, max_length=128)
    usersAssociated = models.JSONField()
