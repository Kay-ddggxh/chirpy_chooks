from django.urls import path
from . import views


urlpatterns = [
    path('', views.entry_list, name="forum"),
    path('<slug:slug>/', views.entry_detail, name='entry_detail'),
    path('create/', views.create_entry, name='create_entry'),
    path('edit/<slug:slug>/', views.edit_entry, name='edit_entry'),
]
