from django.urls import path
from resumesite.views import home

urlpatterns = [
    path('', home, name='home'),
]