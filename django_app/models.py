from django.db import models

# Create your models here.

class mymodel(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta:
        db_table = 'employ' # name of table to be created