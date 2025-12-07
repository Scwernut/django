from django.shortcuts import render, redirect
from .models import MonthRecord, User, Category, Expense
from .forms import MonthRecordForm, UserForm, CategoryForm, ExpenseForm
import matplotlib.pyplot as plt
import numpy as np
import io, urllib, base64
import random
from django.views.decorators.http import require_POST
from django.contrib import messages
def index(request):
    # Айлық деректер
    records = MonthRecord.objects.all()
    record_form = MonthRecordForm()

    # Пайдаланушылар
    users = User.objects.all()
    user_form = UserForm()

    # Категориялар
    categories = Category.objects.all()
    category_form = CategoryForm()

    # Шығындар
    expenses = Expense.objects.all()
    expense_form = ExpenseForm()

    # График
    graph = generate_graph(records)

    context = {
        'records': records,
        'record_form': record_form,
        'users': users,
        'user_form': user_form,
        'categories': categories,
        'category_form': category_form,
        'expenses': expenses,
        'expense_form': expense_form,
        'graph': graph,
    }

    return render(request, 'index.html', context)

# --- График салу ---
def generate_graph(records):
    if not records:
        return None
    months = [r.month for r in records]
    values = [r.value for r in records]
    plt.figure(figsize=(10,5))
    plt.plot(months, values, marker='o')
    plt.title("Айлар бойынша сатылым динамикасы")
    plt.xlabel("Айлар")
    plt.ylabel("Сома (тг)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    buf.close()
    return urllib.parse.quote(string)

# --- Кездейсоқ айлық мәндер жасау ---
def generate_random_data(request):
    months = [
        "Қаңтар", "Ақпан", "Наурыз", "Сәуір", "Мамыр", "Маусым",
        "Шілде", "Тамыз", "Қыркүйек", "Қазан", "Қараша", "Желтоқсан"
    ]
    for m in months:
        value = random.randint(700000, 2000000)
        MonthRecord.objects.update_or_create(month=m, defaults={'value': value})
    return redirect('index')

# --- Айлық дерек қосу ---
def add_record(request):
    if request.method == 'POST':
        form = MonthRecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

# --- Айлық дерек өшіру ---
@require_POST
def delete_record(request, month_id):
    MonthRecord.objects.filter(id=month_id).delete()
    return redirect('index')

# --- Пайдаланушы қосу ---
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

# --- Категория қосу ---
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')




def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            # Пайдаланушының балансын тексеру
            if expense.user.balance < expense.amount:
                messages.error(request, f"Баланс жеткіліксіз! Қолданыстағы баланс: {expense.user.balance} тг")
            else:
                # Балансты азайтып, шығынды сақтау
                expense.user.balance -= expense.amount
                expense.user.save()
                expense.save()
                messages.success(request, f"Шығын қосылды! Жаңа баланс: {expense.user.balance} тг")
        else:
            messages.error(request, "Форма дұрыс емес, барлық өрістерді толтырыңыз.")
    return redirect('index')
from django.views.decorators.http import require_POST

@require_POST
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.success(request, "Пайдаланушы өшірілді!")
    return redirect('index')

@require_POST
def delete_category(request, category_id):
    Category.objects.filter(id=category_id).delete()
    from django.contrib import messages
    messages.success(request, "Категория өшірілді!")
    return redirect('index')

