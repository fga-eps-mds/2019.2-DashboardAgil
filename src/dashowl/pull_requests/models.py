from django.db import models
from ..repositories.models import Repository


class Pull_request(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    pull_request_number = models.IntegerField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    open_date = models.DateTimeField()

    def publish(self):
        self.save()
