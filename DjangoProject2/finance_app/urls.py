from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_record, name='add_record'),
    path('random/', views.generate_random_data, name='generate_random'),
    path('delete/<int:month_id>/', views.delete_record, name='delete_record'),

    path('add_user/', views.add_user, name='add_user'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_expense/', views.add_expense, name='add_expense'),

path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]