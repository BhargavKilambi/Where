from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/home/catalog')

def home(request):
    return redirect('/home/home')
