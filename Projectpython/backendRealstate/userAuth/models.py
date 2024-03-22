from django.db import models
from django.contrib.auth.hashers import make_password



class Role(models.Model):

    name = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    username = None
    role_id = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def set_password(self, password):
        self.password = make_password(password)


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = []


class Temoinage(models.Model):

    name = models.TextField(default='')
    contenu = models.TextField()
    note = models.IntegerField()


class Blog(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Contact(models.Model):
    description = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description