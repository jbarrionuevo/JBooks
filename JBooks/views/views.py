from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world!!!!!!!!!!")

def hopefully(request):
    return HttpResponse("We have a lot of hope in future!!!!!!!! ")