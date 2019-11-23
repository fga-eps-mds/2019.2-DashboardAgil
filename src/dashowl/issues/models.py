from django.db import models
from ..repositories.models import Repository

class Issue(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    issue_number = models.IntegerField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    date = models.DateTimeField()


    def publish(self):
        self.save()

