from django.db import models

from apps.users.models.visitor import Visitor


class VisitorIngress(models.Model):
    """ VisitorIngress model."""

    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)
    ingress_time = models.DateTimeField('Ingress time', auto_now_add=True)
    egress_time = models.DateTimeField('Egress time', blank=True, null=True)
    is_inside = models.BooleanField('Is inside', default=True)

    class Meta:
        """ Meta class."""

        verbose_name = 'Visitor Ingress'
        verbose_name_plural = 'Visitors Ingress'
        db_table = 'visitors_ingress'
        ordering = ['-ingress_time']

    def __str__(self):
        """ String representation."""
        return f"{self.visitor.name} - {self.ingress_time}"
