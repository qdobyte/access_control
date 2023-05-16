from django.db import models


class Employee(models.Model):
    """ Employee model."""

    first_name = models.CharField('First name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    document = models.CharField('Document', max_length=255, unique=True)
    cost_department = models.ForeignKey('users.CostDepartment', on_delete=models.CASCADE, verbose_name='Cost department')
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
        return f"{self.first_name} {self.last_name} ({self.cost_department.name})"
