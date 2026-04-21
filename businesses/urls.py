from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('business/<slug:slug>/', views.business_detail, name='business_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('plans/', views.plans, name='plans'),
]
