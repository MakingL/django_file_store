from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

from file_store_app.models import UploadedFile
from .forms import UploadFileForm


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        upload_form = UploadFileForm(request.POST, request.FILES)
        if not upload_form.is_valid():
            return JsonResponse({"code": "400", "msg": "Invalid data"})

        upload_form.save()
        return JsonResponse({"code": "200", "msg": "OK"})
    else:
        return HttpResponse(status=406)


@csrf_exempt
def get_file_lists(request):
    if request.method == "GET":
        file_list = UploadedFile.objects.get_file_list()
        return JsonResponse({"code": "200", "results": file_list})
    else:
        return HttpResponse(status=406)


def download_file(request, file_name=None):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    if request.method == "GET":
        if not file_name:
            return JsonResponse({"code": "400"})

        file_path = UploadedFile.get_file_path(file_name)
        if not file_path:
            return JsonResponse({"code": "401", "msg": "file doesn't exist"})

        response = StreamingHttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response
    else:
        return HttpResponse(status=406)


def delete_file(request, file_name=None):
    if request.method == "GET":
        if not file_name:
            return JsonResponse({"code": "400"})

        if not UploadedFile.delete_file(file_name):
            return JsonResponse({"code": "401", "msg": "file doesn't exist"})
        else:
            return JsonResponse({"code": "200", "msg": "OK"})
    else:
        return HttpResponse(status=406)
