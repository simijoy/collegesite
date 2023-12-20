from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City


# Create your views here.
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' order confirmed')
            return redirect('person_add')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})


# AJAX
def load_cities(request):
    department_id = request.GET.get('department_id')
    cities = City.objects.filter(department_id=department_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})

def demo(request):
    return render(request, "home.html")

def button(request):
    messages.info(request, 'order confirmed')
    return render(request, 'form.html')
def form(request):
    return render(request,'form.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)

        if user1 is not None:
            auth.login(request, user1)
            return redirect('login/button')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['cpassword']
        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('login')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password is not matching')
            return redirect('login')


    return render(request, 'register.html')

