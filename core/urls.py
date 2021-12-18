from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',  TemplateView.as_view(template_name='core/index.html'), name='HomeView'),
    path('brands',  TemplateView.as_view(template_name='core/brands.html'), name='BrandsView'),
    path('brand-detail',  TemplateView.as_view(template_name='core/brand-detail.html'), name='BrandDetailView'),

]
