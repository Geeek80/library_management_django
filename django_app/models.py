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
    course = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    enrollment = models.CharField(max_length=15)
    password = models.CharField(max_length=21, null=True, blank=True)
    phone_no = models.CharField(max_length=13, null=True)
    parents_phone_no = models.CharField(max_length=13)
    resi_address = models.CharField(max_length=150)
    semester = models.IntegerField()
    division = models.CharField(max_length=5)
    rollno = models.IntegerField()
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
    date = models.DateTimeField(auto_now_add = True)
    receipt_no = models.IntegerField(null=True, blank=True)
    receipt_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField()
    application_no = models.CharField(max_length=15, unique=True)
    student_enrollment= models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, blank=True)
    reason = models.CharField(max_length=256, null=True)
    action_date = models.DateTimeField(blank = True, null=True)
    fee_receipt_image = models.FileField(upload_to="images/", blank=True)
    cancelled_cheque_image = models.FileField(upload_to="images/")
    passbook_image = models.FileField(upload_to="images/")
    last_sem_fee_image = models.FileField(upload_to="images/", blank=True)
    grade_history_image = models.FileField(upload_to="images/")
    
    class Meta:
        db_table = "transaction"
    