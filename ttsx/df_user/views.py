from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'df_user/login.html')


def register(request):
    return render(request, 'df_user/register.html')