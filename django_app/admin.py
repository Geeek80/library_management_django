from django.contrib import admin, messages
from .models import mymodel, student
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
            )
        self.message_user(request, 'the data has been uploaded')
        return HttpResponseRedirect('./')

# Register your models here.
admin.site.register(mymodel)
admin.site.register(student, studentadmin)