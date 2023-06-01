from django.contrib import admin

# Register your models here.
from app.models import student
class studentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
admin.site.register(student,studentAdmin)