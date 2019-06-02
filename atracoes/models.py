from django.db import models

class Atracoes(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    working_time = models.TextField()
    minimal_age = models.TextField()
    
    def __str__(self):
        return self.name
