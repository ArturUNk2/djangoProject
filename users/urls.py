from django.urls import path
from .views import registerview,loginview
urlpatterns = [

    path('register/', registerview),
    path('login/', loginview),



]