from django.urls import path
from interior_app import views

urlpatterns = [
    path("",views.home_view,name="my_home")
]