from django.db import models
from discover.models import User

class Graph(models.Model):
        name = models.CharField(max_length=32)
        creator = models.ForeignKey(User, on_delete=models.CASCADE)
        state = models.JSONField()

        def __str__(self):
                return f"{self.name} | {self.creator}"