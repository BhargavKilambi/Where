from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/profile')

def home(request):
    return redirect('/home')
