from django.db import models

# Create your models here.
#job

'''
 django model field : 
    - html widget
    - validation 
    - db size 
'''

class Job(models.Model): 
    title = models.CharField(max_length=100)  # column
def __str__(self):
    return self.title
    