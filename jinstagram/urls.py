
from django.contrib import admin
from django.urls import path,include
from jinstagram import views

urlpatterns = [
    path('',views.sub.as_view())
]
