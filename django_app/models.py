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

class librarian(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=21)
    email = models.EmailField()
    class Meta:
        db_table = 'librarian'

class transaction(models.Model):
    date = models.DateTimeField(auto_now = True)
    receipt_no = models.IntegerField(blank=True)
    receipt_date = models.DateField()
    amount = models.IntegerField()
    student_enrollment= models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, blank=True)
    fee_receipt_image = models.FileField(upload_to="images/", blank=True)
    cancelled_cheque_image = models.FileField(upload_to="images/")
    passbook_image = models.FileField(upload_to="images/")
    last_sem_fee_image = models.FileField(upload_to="images/", blank=True)
    grade_history_image = models.FileField(upload_to="images/")
    
    class Meta:
        db_table = "transation"
    