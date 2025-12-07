from django.db import models

class MonthRecord(models.Model):
    month = models.CharField(max_length=20, unique=True)
    value = models.FloatField()

    def __str__(self):
        return f"{self.month}: {self.value} тг"

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=20)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} тг"
