from django.db import models


class Milestone(models.Model):
    # repoID = models.ForeignKey(Repository)
    milestoneID = models.IntegerField()
    state = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=60)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()

    def publish(self):
        self.save()
