from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=10)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + ' -- ' + self.email