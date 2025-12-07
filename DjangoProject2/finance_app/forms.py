from django import forms
from .models import MonthRecord, User, Category, Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'category', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Сипаттама'}),
        }

class MonthRecordForm(forms.ModelForm):
    class Meta:
        model = MonthRecord
        fields = ['month', 'value']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'balance']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'category', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Сипаттама'}),
        }
