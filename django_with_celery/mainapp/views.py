from django.shortcuts import render,HttpResponse
from .tasks import task_func

def test(request):
    task_func.delay()
    return HttpResponse("done")