from django.db import models

class Issues(models.Model):
    # repoID = models.ForeignKey(Repository)
    issue_number = models.IntegerField()
    state = models.IntegerField()
    date = models.DateTimeField()


    def publish(self):
        self.save()

