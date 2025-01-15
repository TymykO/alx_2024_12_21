from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def hello_name(request, name):
    return HttpResponse(f"Hello, {name}")