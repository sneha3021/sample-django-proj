from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sell/',views.sell,name='sell'),
    path('buy/',views.buy,name='buy'),
]
