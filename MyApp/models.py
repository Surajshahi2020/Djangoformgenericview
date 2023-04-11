from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name