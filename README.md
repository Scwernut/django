ФУНКЦИОНАЛ МҮМКІНДІКТЕРІ
------------------------

1. SQLite дерекқор
   - Жоба SQLite дерекқорын қолданады (db.sqlite3).

2. Айлық мәндер (MonthRecord)
   - Ай аты мен мәнін қосу
   - Айларды тізімдеу
   - Айларды өшіру
   - Графикте пайдалану

3. NumPy + Matplotlib графигі
   - Айлық мәндер арқылы сызықтық график генерацияланады
   - График Django бетінде көрсетіледі

4. Пайдаланушылар (User)
   - Қосу
   - Тізімдеу
   - Өшіру

5. Категориялар (Category)
   - Қосу
   - Тізімдеу
   - Өшіру

6. Шығындар (Expense)
   - Қосу (пайдаланушы + категория + сома)
   - Тізімдеу
   - Өшіру


ЖОБА ҚҰРЫЛЫМЫ
-------------

finance_project/
    finance_app/
        migrations/
        static/
        templates/
            index.html
        models.py
        views.py
        urls.py
        admin.py
    finance_project/
        settings.py
        urls.py
        wsgi.py
    db.sqlite3
    manage.py
    README.txt


ОРНАТУ ЖӘНЕ ІСКЕ ҚОСУ
---------------------

1. Репозиторийді клондау:
   git clone https://github.com/username/finance_project.git
   cd finance_project

2. Тәуелділіктерді орнату:
   pip install -r requirements.txt

   немесе қолмен:
   pip install django numpy matplotlib

3. Миграция жасау:
   python manage.py migrate

4. Серверді іске қосу:
   python manage.py runserver

5. Браузерден ашу:
   http://127.0.0.1:8000/


НЕГІЗГІ ФАЙЛДАР
---------------

models.py:
 - User
 - Category
 - Expense
 - MonthRecord

views.py:
 - index
 - add_user
 - add_category
 - add_expense
 - add_month
 - delete_user
 - delete_category
 - delete_expense
 - delete_month
 - График генерациялау коды

templates/index.html:
 - Айларды шығару
 - Шығындар
 - Пайдаланушылар
 - Категориялар
 - Форма арқылы қосу
 - Өшіру батырмалары
 - Графикті шығару


ГРАФИК ГЕНЕРАЦИЯСЫ
------------------

Matplotlib графигі views.py ішінде Base64 форматында HTML-ге беріледі.
