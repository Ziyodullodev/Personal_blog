from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('about/', about,  name='about'),
    path('books/', books, name='books'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/', blogdetail, name='blogdetail'),
]