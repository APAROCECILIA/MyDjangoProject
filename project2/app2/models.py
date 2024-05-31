from django.db import models
import datetime

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)
    
    def __str__(self):
        return self.top_name

class webPage(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class AccessRecords(models.Model):
    name = models.ForeignKey(webPage, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today) 
    
    def __str__(self):
        return str(self.date)
    
    