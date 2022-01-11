from django.db import models


class Commercial(models.Model):
    session_id = models.CharField(max_length=100, default='', blank=False)
    step = models.IntegerField(default=0, blank=False)
    address = models.CharField(max_length=100, default='', blank=True)
    experience = models.CharField(max_length=100, default='', blank=True)
    first_name = models.CharField(max_length=100,  default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    company_name = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
