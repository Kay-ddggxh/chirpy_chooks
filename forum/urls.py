from django.urls import path
from . import views


urlpatterns = [
    path('', views.entry_list, name="forum"),
    path('create/', views.create_entry, name='create_entry'),
    path('<slug:slug>/', views.entry_detail, name='entry_detail'),
]
