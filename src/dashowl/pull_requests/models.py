from django.db import models

class Pull_request(models.Model):
    # repoID = models.ForeignKey(Repository)
    pullRequestID = models.IntegerField()
    openedPullRequests = models.IntegerField()
    closedPullRequests = models.IntegerField()
    totalPullRequests = models.IntegerField() 

    def publish(self):
        self.save()