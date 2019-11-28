from django.db import models
from ..repositories.models import Repository


class Commit(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    sha_commit = models.CharField(max_length=60)
    author = models.CharField(max_length=50)
    date = models.DateTimeField()

    def publish(self):
        self.save()
