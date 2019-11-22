from django.db import models

class Issues(models.Model):
    # repoID = models.ForeignKey(Repository)
    issue_number = models.IntegerField()
    state = models.CharField(max_length=20)
    date = models.DateTimeField()


    def publish(self):
        self.save()

