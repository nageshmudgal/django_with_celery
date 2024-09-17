from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import task_func
from send_mail.tasks import send_mail_func

# Create your views here.
def test(request):
    task_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")