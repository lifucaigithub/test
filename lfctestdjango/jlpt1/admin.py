

# Register your models here.
from django.contrib import admin
from models import ExamInfo

# Register your models here.

class ExamInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
admin.site.register(ExamInfo, ExamInfoAdmin)