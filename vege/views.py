from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()


#To send mail
def send_email(request):

    subject = "This email is from django server"
    message = "This mail is for testing the mailing with attachments"
    recipient_list = ["sukshamarya00007@gmail.com"]
    file_path = f'{settings.BASE_DIR}/public/static/recipe/assign.png'

    # send_email_to_client()
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')

#To get the list of all recipes
@login_required(login_url = '/login/')
def recipes(request):

    if request.method == 'POST':

        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )

        return redirect('/recipes')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipes': queryset}

    return render(request, 'recipes.html', context)


#To delete a particular recipe
@login_required(login_url = '/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect('/recipes')


#To update a particular recipe
@login_required(login_url = '/login/')
def update_recipe(request, slug):
    queryset = Recipe.objects.get(slug=slug)

    if request.method == 'POST':

        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes')

      
    context = {'recipe' : queryset}

    return render(request, 'update_recipe.html', context)



#User login
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Credentials un')
            return redirect('/login/')

        user = authenticate(username = username, password = password)
        print(user)
        print(username, password)
        if user is None:
            messages.error(request, 'Invalid Credentials pw')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')



    return render(request, 'login.html')


#User logout
def logout_page(request):
    logout(request)
    return redirect('/login') 


#User registration page
def register_page(request):
#    redirect_count = int(request.GET.get('redirect_count', 0))

   if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')

        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

   return render(request, 'register.html')



#To get the list of students
def get_students(request):
    queryset = Student.objects.all()


    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)
        )
    
    paginator = Paginator(queryset, 10) 

    page_number = request.GET.get("page", 1)  #1 for the default case
    page_obj = paginator.get_page(page_number)

    print(page_obj.object_list)

    return render(request, 'report/students.html', {'queryset': page_obj})


#To get the marks of a particular student
from .seed import generate_report_card
def get_marks(request, student_id):
    # generate_report_card()

    queryset = SubjectMark.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))

    # current_rank = -1
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    # i = 1

    # for rank in ranks:
    #     if student_id == rank.student_id.student_id:
    #         current_rank = i
    #         break
    #     i+=1

    return render(request, 'report/get_marks.html', {'queryset' : queryset , 'total_marks' : total_marks})

# , 'current_rank' : current_rank