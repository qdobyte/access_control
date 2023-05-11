from django.db import models


class CostDepartment(models.Model):
    """ Cost Department model. """

    name = models.CharField('Name', max_length=100, unique=True)
    description = models.TextField('Description', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField('Create date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    class Meta:
        """ Meta class. """

        verbose_name = 'Cost Department'
        verbose_name_plural = 'Cost Departments'
        db_table = 'cost_departments'
        ordering = ['-created_at']

    def __str__(self):
        """ String representation."""
        return self.name

