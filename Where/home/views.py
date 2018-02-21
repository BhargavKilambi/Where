from django.shortcuts import render,redirect
from .models import Places,Goods
from .forms import RegistrationForm,EditProfileForm,AddGoodsForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from geoposition.forms import GeopositionField
from django import forms
from django.contrib.auth import authenticate, login
# Create your views here.

# def home(request):
#     return redirect('home/home.html')

def about(request):
    return render(request,'home/about.html')

@login_required
def editit(request):
    return render(request,'home/catalog.html')

@login_required
def myProfile(request):
    curr_user = request.user
    place  = Places.objects.filter(user=curr_user)
    good = Goods.objects.filter(user=curr_user)
    return render(request,'home/profile.html',{'place':place,'good':good})

def show_places(request):
    goods = Goods.objects.all()
    arg = {'goods':goods}
    return render(request,'home/home.html',arg)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/regloc')
    else:
        form = RegistrationForm()


    return render(request,'home/reg_form.html',{'form':form})


def search(request):
    query = request.GET.get("q")
    if query:
        items = Goods.objects.filter(Q(name__icontains=query)|Q(price__icontains=query)).distinct()

    return render(request,'home/home.html',{'items':items})

@login_required
def addgoods(request):
    if request.method == 'POST':
        form = AddGoodsForm(request.POST)
        if form.is_valid():
            good = form.save(commit=False)
            good.user = request.user
            good.save()
            return redirect('/profile')
    else:
        form = AddGoodsForm()


    return render(request,'home/add_good.html',{'form':form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'home/edit_profile.html', args)


# class TestForm(forms.ModelForm):
#     geo_position_field = GeopositionField()
#     title = forms.CharField(max_length=200,required=True)
#     class Meta:
#         model = Places
#         fields = ('geo_position_field',
#                 'title',)
#
#
# def add_route(request):
#     if request.method == 'POST':
#         form = TestForm(request.POST, instance = request.user.places)
#         if form.is_valid():
#             good = form.save(commit=False)
#             good.user = request.user
#             good.save()
#             return redirect('/profile')
#     else:
#         form = TestForm()
#
#
#     return render(request,'home/reg_profile.html',{'form':form})


def editProfile(request):
    if request.method == 'POST':
        form = PlacesForm(request.POST,instance=request.user)

        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.save()
            return redirect('/profile')

    else:
        form = PlacesForm()

    return render(request,'home/reg_profile.html',{'form':form})
