from django.db import models

# Create your models here.

class mymodel(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.FileField(upload_to='image/')
    # date = models.DateTimeField() # for date type column
    class Meta:
        db_table = 'employ' # name of table to be created
        ordering = [ '-ename' ] # sorting enames by descending order wherever they're displayed