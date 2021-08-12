from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.email