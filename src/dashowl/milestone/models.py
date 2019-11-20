from django.db import models
from django.utils import timezone

class Milestones(models.Model):
    # repoID = models.ForeignKey(Repository)
    title = models.CharField(max_length=200)
    due_on = models.DateTimeField()

    def publish(self):
        self.save()
