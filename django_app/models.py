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

class student(models.Model):
    name = models.CharField(max_length=20)
    enrollment = models.CharField(max_length=15)
    password = models.CharField(max_length=21)
    email = models.EmailField()
    class Meta:
        db_table = 'student'

class transaction(models.Model):
    application_no = models.IntegerField(null=True, blank=True, unique=True)
    date = models.DateTimeField(auto_now = True)
    receipt_no = models.IntegerField()
    receipt_date = models.DateField()
    amount = models.IntegerField()
    student_enrollment= models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    fee_receipt_image = models.FileField(upload_to="images/")
    cancelled_cheque_image = models.FileField(upload_to="images/")
    
    class Meta:
        db_table = "transation"
    