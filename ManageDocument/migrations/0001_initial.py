# Generated by Django 3.1 on 2021-05-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('requestID', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=32)),
                ('title', models.TextField(max_length=100)),
                ('fingerprintCreated', models.CharField(max_length=32)),
                ('fingerprintCompleted', models.CharField(max_length=32)),
                ('fingerprintsPerAction', models.JSONField()),
                ('documentProcess', models.IntegerField()),
                ('dateCreatedBy', models.CharField(max_length=32)),
                ('dateLastEdited', models.CharField(max_length=32)),
                ('associatedWith', models.JSONField()),
                ('timeAddedTo', models.JSONField()),
                ('timeViewedBy', models.JSONField()),
                ('timeSignedBy', models.JSONField()),
                ('actionAtIPList', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentBlock',
            fields=[
                ('userIDNonce', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('blockAddress', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDrafts',
            fields=[
                ('userIDNonce', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('documentKey', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('userID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('documents', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsCompleted',
            fields=[
                ('userIDNonce', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('documentKey', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsReceived',
            fields=[
                ('userIDNonce', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('documentKey', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsSent',
            fields=[
                ('userIDNonce', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('documentKey', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfDocumentDrafts',
            fields=[
                ('userID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('documents', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfDocumentsCompleted',
            fields=[
                ('userID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('documents', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfDocumentsReceived',
            fields=[
                ('userID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('documents', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfDocumentsSent',
            fields=[
                ('userID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('documents', models.IntegerField(default=0)),
            ],
        ),
    ]
