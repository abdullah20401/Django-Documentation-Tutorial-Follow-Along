import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=25)
    dob = models.DateField()
    pub_date = models.DateTimeField('Date Published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name + ' - ' + self.dob
