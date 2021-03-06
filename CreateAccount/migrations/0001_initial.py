# Generated by Django 3.0.7 on 2021-09-29 20:42

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('userID', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('lastLoginTime', models.CharField(max_length=16)),
                ('currentIP', models.CharField(max_length=32)),
                ('signature1', models.ImageField(upload_to='')),
                ('signature2', models.ImageField(upload_to='')),
                ('signature3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AccountLookup',
            fields=[
                ('userID', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('key', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('users', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('userOwnerEmail', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('teamsAssociated', django_mysql.models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('userOwnerEmail', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('branchesAssociated', django_mysql.models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('userOwnerEmail', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('usersAssociated', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
