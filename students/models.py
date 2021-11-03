from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    address = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
