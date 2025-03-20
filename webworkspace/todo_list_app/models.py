from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=100, null=True)
    due = models.DateField(null=True)  # Use DateField for proper date validation

    def __str__(self):
        return f"{self.todo} - {self.due.strftime('%m/%d/%Y')}"
