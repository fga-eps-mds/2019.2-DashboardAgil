from django.db import models

class Commit(models.Model):
    # repoID = models.ForeignKey(Repository)
    shaCommit = models.CharField(max_length=60)
    author = models.CharField(max_length=50)

    def publish(self):
        self.save()
