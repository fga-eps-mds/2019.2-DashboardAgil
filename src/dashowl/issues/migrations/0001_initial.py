# Generated by Django 2.2.7 on 2019-11-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issueID', models.IntegerField()),
                ('totalIssues', models.IntegerField()),
            ],
        ),
    ]
