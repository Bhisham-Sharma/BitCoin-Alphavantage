from django.db import models

class Price(models.Model):
    date = models.CharField(max_length=30)
    open_price = models.CharField(max_length=30)
    close_price = models.CharField(max_length=30)

    class Meta:
        app_label = 'app'

