from django.db import models


class CostCenter(models.Model):
    """ Cost Center model. """

    name = models.CharField('Name', max_length=100, unique=True)
    description = models.TextField('Description', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField('Create date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    class Meta:
        """ Meta class. """

        verbose_name = 'Cost Center'
        verbose_name_plural = 'Cost Centers'
        db_table = 'cost_centers'
        ordering = ['-created_at']

    def __str__(self):
        """ String representation."""
        return self.name

