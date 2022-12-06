from django.db import models


class Subscriber(models.Model):
    """ Newsletter subscriber model """

    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
