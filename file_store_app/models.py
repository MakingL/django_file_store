import os

from django.db import models
from django.dispatch import receiver

from file_store.settings import FILES_STORE_DIR


class UploadedFileManager(models.Manager):
    def get_file_list(self):
        return [os.path.basename(file_path) for file_path in self.values_list("uploaded_file", flat=True)]


class UploadedFile(models.Model):
    uploaded_file = models.FileField(verbose_name="上传的文件", upload_to=FILES_STORE_DIR)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    objects = UploadedFileManager()

    def __str__(self):
        return self.uploaded_file.name

    class Meta:
        verbose_name = verbose_name_plural = "上传的文件"
        ordering = ['-create_time']
        app_label = "file_store_app"
        db_table = "uploaded_file"

    @classmethod
    def get_file_path(cls, file_name):
        file_path = "{}/{}".format(FILES_STORE_DIR, file_name)
        if not cls.objects.filter(uploaded_file=file_path).exists():
            return None
        return file_path

    @classmethod
    def delete_file(cls, file_name):
        file_path = "{}/{}".format(FILES_STORE_DIR, file_name)
        filter_res = cls.objects.filter(uploaded_file=file_path)
        if not filter_res.exists():
            return False
        else:
            filter_res.delete()
            return True


@receiver(models.signals.post_delete, sender=UploadedFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.uploaded_file:
        if os.path.isfile(instance.uploaded_file.path):
            os.remove(instance.uploaded_file.path)
