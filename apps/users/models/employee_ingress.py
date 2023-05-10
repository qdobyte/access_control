from django.db import models

from apps.users.models import Employee


class EmployeeIngress(models.Model):
    """ EmployeeIngress Model."""

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    ingress_time = models.DateTimeField('Ingress time', auto_now_add=True)
    egress_time = models.DateTimeField('Egress time', blank=True, null=True)
    is_inside = models.BooleanField('Is inside', default=True)

    class Meta:
        """ Meta class."""

        verbose_name = 'Employee Ingress'
        verbose_name_plural = 'Employees Ingress'
        db_table = 'employees_ingress'
        ordering = ['-ingress_time']

    def __str__(self):
        """ String representation."""
        return f"{self.employee.name} - {self.ingress_time}"


