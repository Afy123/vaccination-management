from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from vaccineapp.forms import LoginRegister, NurseRegister, UserRegister


def index(request):
    return render(request, 'Home/index.html')


def AdminPanel(request):
    return render(request, 'AdminPanel/AdminPanel.html')


def NursePanel(request):
    return render(request, 'NursePanel/NursePanel.html')


def UserPanel(request):
    return render(request, 'UserPanel/UserPanel.html')


def Login(request):
    return render(request, 'LoginPage/login.html')


def Nurse_register(request):
    login_form = LoginRegister()
    nurse_form = NurseRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        nurse_form = NurseRegister(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            u = login_form.save(commit=False)
            u.is_nurse = True
            u.save()
            n = nurse_form.save(commit=False)
            n.User = u
            n.save()
            return redirect('NursePanel')
    return render(request, 'Nurse/nurse_registration.html', {'login_form': login_form, 'nurse_form': nurse_form})


def User_register(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            l = login_form.save(commit=False)
            l.is_user = True
            l.save()
            u = user_form.save(commit=False)
            u.User = l
            u.save()
            return redirect('UserPanel')
    return render(request, 'User/user_registration.html', {'login_form': login_form, 'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('AdminPanel')
            elif user.is_nurse:
                return redirect('NursePanel')
            elif user.is_user:
                return redirect('UserPanel')
    return render(request, 'LoginPage/login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')
