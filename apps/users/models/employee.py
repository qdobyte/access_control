from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """ Employee model."""

    name = models.CharField('Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    document = models.CharField('Document', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    cost_center = models.ForeignKey('users.CostCenter', on_delete=models.CASCADE, verbose_name='Cost Center')
    created_at = models.DateTimeField('Create date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    class Meta:
        """ Meta class."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table = 'employees'
        ordering = ['-id']

    def __str__(self):
        """ String representation."""
        return self.user.get_full_name()
