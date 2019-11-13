from django.db import models

class Commit(models.Model):
    commitID = models.IntegerField()
    totalCommits = models.IntegerField()
    author = models.CharField(max_length=50)

    