from django import forms
from .models import *


class BrandFrom(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'PO': forms.Select(attrs={'class': 'form-control'}),
            'scrum_master': forms.Select(attrs={'class': 'form-control'}),
            # 'logo': forms.FileField(attrs={'class': 'form-control'}),
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
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'completion': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'
        widgets = {
            'Quarter': forms.Select(attrs={'class': 'form-control'}),
            'Brand': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'SubObjective': forms.Select(attrs={'class': 'form-control'}),
        }
