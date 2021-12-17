from django.shortcuts import render
from core.models import *
# Create your views here.


def home(request):
    brands = Brand.objects.all()