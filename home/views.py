from django.shortcuts import render
from django.http import HttpResponse
from vege.seed import *
import random
from .models import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

# Create your views here.
def home(request):
    # seed_db(100)
    # return HttpResponse("This is a home page.")

    # Car.objects.create(car_name = f"Nexon-{random.randint(0,100)}") #signals 
    people = [
        {"name" : "arya", "age" : 23},
        {"name" :"suksham", "age" : 24},
        {"name" :"simran", "age" : 25},
        {"name" :"kashish", "age" : 17},
        {"name" :"radha", "age" : 11},
        {"name" :"kavita", "age" : 31},
    ]

    text = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla, nostrum? Id natus deleniti suscipit, omnis perspiciatis tempora odio excepturi nulla dicta ipsum, ad iste fugit dolores itaque illum nemo! Molestiae saepe corporis quibusdam quaerat, labore nisi vel quidem debitis, illo itaque commodi incidunt, hic veniam laboriosam possimus praesentium. Eveniet in praesentium nisi minus inventore exercitationem necessitatibus quod, maiores expedita obcaecati asperiores sed nesciunt distinctio aspernatur saepe porro sit reprehenderit ut harum ab voluptatum quis dolorum sapiente. Omnis, repudiandae. Earum saepe consequatur nostrum tempore ullam accusamus, et tenetur dolores fugiat dolor, voluptatibus nihil officiis est voluptatum corrupti vero repudiandae dolorem consectetur!'''

    vegetables = ['Tomato', 'Pumpkin', 'potato', 'Aubergine']
    return render(request, 'home/index.html', context = {'people' : people, 'text' : text, 'vegetables' : vegetables, 'page' : 'Django-2023-Home'})


def page(request):
    print("*" * 10)
    return HttpResponse("This is just page")


def about(request):
    context = {'page' : 'About'}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'home/contact.html', context)


def info(request):
    return HttpResponse("This is API response.")


#Building simple APIs in Django:
@api_view(['GET'])
def getData(request):
    app = Product.objects.all()
    serializer = ProductSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = ProductSerializer(data=request.data)
    print(request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

