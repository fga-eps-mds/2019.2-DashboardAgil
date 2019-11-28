from django.db import models
from ..index.models import Usuario


class Repository(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    repositoryID = models.IntegerField()

    def publish(self):
        self.save()