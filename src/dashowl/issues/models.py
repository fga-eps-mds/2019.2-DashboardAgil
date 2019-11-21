from django.db import models

class Commit(models.Model):
    # repoID = models.ForeignKey(Repository)
    issueID = models.IntegerField()
    totalIssues = models.IntegerField()

    def publish(self):
        self.save()