# Generated by Django 2.2.7 on 2019-11-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pull_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pullRequestID', models.IntegerField()),
                ('openedPullRequests', models.IntegerField()),
                ('closedPullRequests', models.IntegerField()),
                ('totalPullRequests', models.IntegerField()),
            ],
        ),
    ]
