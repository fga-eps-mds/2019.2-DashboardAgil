from django.db import models
from ..repositories.models import Repository


class Milestone(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    milestoneID = models.IntegerField()
    state = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=60)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()

    def publish(self):
        self.save()
