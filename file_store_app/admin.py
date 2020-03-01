from django.contrib import admin

from .models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ("uploaded_file", "update_time", "create_time")
    fields = ("uploaded_file",)
