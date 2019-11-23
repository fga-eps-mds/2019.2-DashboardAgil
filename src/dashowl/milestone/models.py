from django.db import models


class Milestones(models.Model):
    # repoID = models.ForeignKey(Repository)
    milestoneID = models.IntegerField()
    state = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    due_on = models.DateTimeField()

    def publish(self):
        self.save()
