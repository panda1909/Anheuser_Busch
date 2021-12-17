from django import forms
from .models import *


class BrandFrom(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileField(attrs={'class': 'form-control'}),
        }


class ObjectiveFrom(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'
        widgets = {
            'Brand': forms.Select(attrs={'class': 'form-control'}),
            'Quarter': forms.Select(attrs={'class': 'form-control'}),
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'completion': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SubObjectiveForm(forms.ModelForm):
    class Meta:
        model = SubObjective
        fields = '__all__'
        widgets = {
            'Objective_fk': forms.Select(attrs={'class': 'form-control'}),
            'Sprint': forms.Select(attrs={'class': 'form-control'}),
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'completion': forms.BooleanField(attrs={'class': 'form-control'}),
        }