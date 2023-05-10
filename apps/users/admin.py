from django.contrib import admin


from apps.users.models import CostCenter, Employee, EmployeeIngress, Visitor, VisitorIngress


admin.site.register(CostCenter)
admin.site.register(Employee)
admin.site.register(EmployeeIngress)
admin.site.register(Visitor)
admin.site.register(VisitorIngress)


