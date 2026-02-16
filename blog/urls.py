
from django.urls import path
from .views import blog,all_countries ,product_detail
urlpatterns = [

    path('', blog),
    path('next_to_page/', all_countries, name='products'),
    path('next_to_page/<int:id>/',product_detail, name="Detail"),



]