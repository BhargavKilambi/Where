from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile,Goods
from geoposition.fields import GeopositionField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'email',
                'password1',
                'password2',
            )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class AddGoodsForm(forms.ModelForm):
    name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Name"
        }
    ))
    price = forms.DecimalField(max_digits=7,decimal_places=2,required=True,widget=forms.NumberInput(
    attrs = {
        'class' :'form-control',
        'placeholder' : "Price"
        }
    ))
    stock = forms.IntegerField(required=True,widget=forms.NumberInput(
    attrs = {
        'class' :'form-control',
        'placeholder' : "Stock"
        }
    ))
    out_of = forms.IntegerField(required=True,widget=forms.NumberInput(
    attrs = {
        'class' :'form-control',
        'placeholder' : "Out of"
        }
    ))
    #position = GeopositionField
    class Meta:
        model = Goods
        fields = (
            'name',
            'price',
            #'position',
            'stock',
            'out_of'
        )

class PlacesForm(forms.ModelForm):
    title = forms.CharField(max_length=200,required=True)
    position = GeopositionField

    class Meta:
        model = UserProfile
        fields = ('title',
                  'des',
                  'phone',
                  'position',)

    def save(self,commit=True):
        user = super(PlacesForm, self).save(commit=False)
        user.title = self.cleaned_data['title']

        if commit:
            user.save()

        return user
