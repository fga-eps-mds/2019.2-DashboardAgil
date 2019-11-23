from django.db import models

class Issue(models.Model):
    # repoID = models.ForeignKey(Repository)
    issue_number = models.IntegerField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    date = models.DateTimeField()


    def publish(self):
        self.save()

