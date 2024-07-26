from django.db import models



class Expense(models.Model):
    TITLE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=7, choices=TITLE_CHOICES)

    def __str__(self):
        return f'{self.title} - {self.amount}'

