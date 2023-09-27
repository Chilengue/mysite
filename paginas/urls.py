from django.urls import path
from .views import IndexView

urlpatterns = [
    path('inicio/', IndexView.as_View(), name='inicio'),  
]


