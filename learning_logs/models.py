from django.db import models

# Create your models here.

class Topic(models.Model):
    """Temat poznawany przez użytkownika."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
    return self.text

