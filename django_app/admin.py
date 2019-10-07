from django.contrib import admin, messages
from .models import mymodel, student, request_transaction, book_bank
from django.urls import path
from django.http import HttpResponseRedirect
import io, csv 

admin.site.site_header = "Library Fee Management Admin"

class studentadmin(admin.ModelAdmin):
    change_list_template = "admin/csv.html"
    list_display = [
        'name',
        'enrollment',
        'email',
        'semester'
        ]
    list_filter = ('semester',)
    search_fields = ('name', 'email', 'enrollment')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload_csv', self.upload_csv),
        ]
        return custom_urls + urls
    
    def upload_csv(self, request):
        students = student.objects.all()
        csv_file = request.FILES['document']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "the file is not csv file")
            return HttpResponseRedirect('./')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for col in csv.reader(io_string, delimiter=','):
            if student.objects.filter(enrollment=col[1]).exists():
                messages.error(request, "student with enrollment: {} already exists try changin'".format(col[1]))
                return HttpResponseRedirect('./')
            if student.objects.filter(email=col[8]).exists():
                messages.error(request, "student with email: {} already exists try changin'".format(col[8]))
                return HttpResponseRedirect('./')
            _, created = student.objects.update_or_create(
                name=col[0],
                enrollment=col[1],
                password=col[2],
                phone_no = col[3],
                resi_address = col[4],
                semester = col[5],
                division = col[6],
                rollno = col[7],
                email = col[8],
                stream = col[9],
                parents_phone_no = col[10],
                batch_year = col[11],
            )
        self.message_user(request, 'the data has been uploaded')
        return HttpResponseRedirect('./')

# Register your models here.
admin.site.register(mymodel)
admin.site.register(request_transaction)
admin.site.register(student, studentadmin)
admin.site.register(book_bank)