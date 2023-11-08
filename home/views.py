from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is a home page.")
    return render(request, 'index.html')


def page(request):
    print("*" * 10)
    return HttpResponse("This is just page")
