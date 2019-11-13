from django.db import models

class Pull_request(models.Model):
    pullRequestID = models.IntegerField()
    openedPullRequests = models.IntegerField()
    closedPullRequests = models.IntegerField()
    totalPullRequests = models.IntegerField() 

    def publish(self):
        self.save()