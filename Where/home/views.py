from django.shortcuts import render,redirect
from .models import UserProfile,Goods
from .forms import RegistrationForm,EditProfileForm,AddGoodsForm,PlacesForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from geoposition.forms import GeopositionField
from django import forms
from django.contrib.auth import authenticate, login
# Create your views here.
#from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404


# class ContactView(FormView):
#     template_name = 'home/add_good.html'
#     form_class = AddGoodsForm
#     success_url = reverse_lazy("home:profile")
#
#     def get_form(self,AddGoodsForm):
#         """
#         Check if the user already saved contact details. If so, then show
#         the form populated with those details, to let user change them.
#         """
#         try:
#             good = Goods.objects.get(user=self.request.user)
#             return form_class(instance=contact, **self.get_form_kwargs())
#         except Goods.DoesNotExist:
#             return form_class(**self.get_form_kwargs())
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.save()
#         return super(ContactView, self).form_valid(form)
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
    place  = UserProfile.objects.filter(user=curr_user)
    good = Goods.objects.filter(user=curr_user).order_by('-created_date')
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
            return redirect('/add_loc')
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
            good.position = request.user.userprofile.position
            good.save()
            return redirect('/profile')
    else:
        form = AddGoodsForm()


    return render(request,'home/add_goods.html',{'form':form})

def add_loc(request):
    if request.method == 'POST':
        form = PlacesForm(request.POST,instance=request.user.userprofile)
        if form.is_valid():
            good = form.save(commit=False)
            good.user = request.user
            good.save()
            return redirect('/profile')
    else:
        form = PlacesForm(instance=request.user.userprofile)


    return render(request,'home/reg_profile.html',{'form':form})

@login_required
def addgood(request,pk=None):
    goo = get_object_or_404(Goods,pk=pk)
    if request.method == 'POST':
        form = AddGoodsForm(request.POST,instance=goo)
        if form.is_valid():
            good = form.save(commit=False)
            good.user = request.user
            good.position = request.user.userprofile.position
            good.save()
            return redirect('/profile')
    else:
        form = AddGoodsForm(instance=goo)


    return render(request,'home/add_good.html',{'form':form})

def delete_good(request,pk=None):
    if pk:
        Goods.objects.get(pk=pk).delete()
    else:
        pass
    return redirect('/profile')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        p = PlacesForm(request.POST, instance = request.user.userprofile)
        if form.is_valid() and p.is_valid():
            form.save()
            p.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance = request.user)
        p = PlacesForm(instance = request.user.userprofile)
        args = {'form': form,'p':p}
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
