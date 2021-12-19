from django.urls import path
from django.views.generic import TemplateView
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('brands', brands, name='brands'),
    # Brand Urls
    path('brand-detail/<int:pk>/', view_brand, name='brand-detail'),
    path('create-brand/', create_brand, name='create-brand'),
    path('update-brand/<int:pk>/', update_brand, name='update-brand'),
    # Objective Urls
    path('add-objective/', add_objective, name='add-objective'),
    path('update-objective/<int:pk>/', update_objective, name='update-objective'),
    # path()
    path('add-sprint/', add_sprint, name='add-sprint'),

    path('update-sprint/<int:pk>/', update_sprint, name='update-sprint'),
    path('add-subobjective/', add_sub_objective, name='add-sub-objective'),
    path('update-sub-objective/<int:pk>/', update_sub_objective, name='update-sub-objective'),

    # objective Urls

]
