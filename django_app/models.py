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
    stream = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    enrollment = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=21, null=True, blank=True)
    phone_no = models.CharField(max_length=13, null=True)
    parents_phone_no = models.CharField(max_length=13)
    resi_address = models.CharField(max_length=150)
    batch_year = models.IntegerField()
    semester = models.IntegerField()
    division = models.CharField(max_length=5)
    rollno = models.IntegerField()
    email = models.EmailField(unique=True)
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
    application_no = models.CharField(max_length=15)
    student_enrollment= models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, blank=True)
    additional_information = models.CharField(max_length=150, blank=True, null=True)
    reason = models.CharField(max_length=256, null=True, blank=True)
    action_date = models.DateTimeField(blank = True, null=True)
    fee_receipt_image = models.FileField(upload_to="images/", blank=True)
    cancelled_cheque_image = models.FileField(upload_to="images/")
    passbook_image = models.FileField(upload_to="images/")
    last_sem_fee_image = models.FileField(upload_to="images/", blank=True)
    grade_history_image = models.FileField(upload_to="images/")
    
    class Meta:
        db_table = "transaction"

class counts(models.Model):
    ica_counts = models.IntegerField()
    mca_counts = models.IntegerField()
    class Meta:
        db_table = "counts"

class book_bank(models.Model):
    semester = models.IntegerField()
    stream = models.CharField(max_length=10)
    calender = models.CharField(max_length=10)
    subjects = models.CharField(max_length=60)
    books_names = models.CharField(max_length=200)
    books_ssn_numbers = models.CharField(max_length=40)
    books_authors = models.CharField(max_length=100)
    class Meta:
        db_table = "book_bank"
    