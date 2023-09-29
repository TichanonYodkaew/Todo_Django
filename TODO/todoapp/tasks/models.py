
from django.db import models
from django.utils import timezone


# Create your models here.

class TaskItem(models.Model):
    DEFAULT = 'DEFAULT'
    PERSONAL  =  'PERSONAL'
    SHOPPING = 'SHOPPING'
    WISHLIST = 'WISHLIST'
    WORK =' WORK'
    CATEGORIES = (
        (DEFAULT,DEFAULT),
        (PERSONAL,PERSONAL),
        (SHOPPING,SHOPPING),
        (WISHLIST,WISHLIST),
        (WORK,WORK)
    )
    title = models.CharField(max_length=500,blank=True,null=True)
    description =models.TextField(null= True,blank=True)
    deadline = models.DateField(default= timezone.now)
    task_finished = models.BooleanField(default= False)
    category = models. CharField(max_length= 20, choices= CATEGORIES , default= DEFAULT)

    def __str__(self):
        return f'{self.title}'