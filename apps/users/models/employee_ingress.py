from django.db import models
from apps.users.models import Employee


class EmployeeIngress(models.Model):
    """ EmployeeIngress Model."""

    CITA = 'CITA'
    CALAMIDAD = 'CALAMIDAD'
    DILIGENCIA = 'DILIGENCIA'
    REASON_CHOICES = [
        (CITA, 'Cita médica'),
        (CALAMIDAD, 'Calamidad'),
        (DILIGENCIA, 'Diligencia personal')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    ingress_time = models.DateTimeField('Ingress time', auto_now_add=True)
    egress_time = models.DateTimeField('Egress time', blank=True, null=True)
    is_inside = models.BooleanField('Is inside', default=True)
    reason_for_leaving = models.CharField('Reason for leaving', choices=REASON_CHOICES, max_length=255, blank=True, null=True)

    class Meta:
        """ Meta class."""

        verbose_name = 'Employee Ingress'
        verbose_name_plural = 'Employees Ingress'
        db_table = 'employees_ingress'
        ordering = ['-ingress_time']

    def __str__(self):
        """ String representation."""
        return f"{self.employee.first_name } {self.employee.last_name} ({self.employee.cost_department.name}) - " \
               f"{self.ingress_time.strftime('%Y-%m-%d %H:%M:%S')}"
