from django.db import models


class Visitor(models.Model):
    """ Visitor model. """
    name = models.CharField('Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    document = models.CharField('Document', max_length=255)
    is_provider = models.BooleanField('Is Provider', default=False)
    company = models.CharField('Company', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField('Create date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    class Meta:
        """ Meta class. """
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'
        db_table = 'visitors'
        ordering = ['-created_at']

    def __str__(self):
        """ String representation."""
        return f"{self.name} {self.last_name}"




