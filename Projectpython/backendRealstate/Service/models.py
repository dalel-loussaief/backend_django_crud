from django.db import models

# Create your models here.
class Service(models.Model):
    id_service = models.BigAutoField(primary_key=True)
    type_service = models.CharField(max_length=255)

    def __str__(self):
        return self.type_service