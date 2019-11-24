from django.db import models

class Pull_request(models.Model):
    # repoID = models.ForeignKey(Repository)
    pull_request_number = models.IntegerField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    open_date = models.DateTimeField()

    def publish(self):
        self.save()