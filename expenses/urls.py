from django.urls import path
from .views import get_expenses, add_expense, update_expense, delete_expense

urlpatterns = [
    path('get_expense/', get_expenses, name='get_expenses'),
    path('add_expense/', add_expense, name='add_expense'),
    path('update_expense', update_expense, name='update_expense'),
    path('delete_expense/', delete_expense, name='delete_expense'),
]
