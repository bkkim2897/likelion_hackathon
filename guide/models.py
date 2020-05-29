from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    place = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    tag = models.CharField(max_length = 100)
    content = models.TextField()
    file = models.FileField(null=True)  
