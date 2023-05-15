from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from apps.users.api.views.home import home
from apps.users.api.views.employee import EmployeeViewSet
from apps.users.api.views.visitor import VisitorViewSet
from apps.users.api.views.cost_department import CostDepartmentViewSet
from apps.users.api.views.employee_ingress import EmployeeIngressViewSet
from apps.users.api.views.visitor_ingress import VisitorIngressViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', home, name='home'),
    path('api/v1/employee/create/', EmployeeViewSet.as_view({'post': 'create'}), name='create_employee'),
    path('api/v1/employee/list/', EmployeeViewSet.as_view({'get': 'list'}), name='list_employee'),
    path('api/v1/visitor/create/', VisitorViewSet.as_view({'post': 'create'}), name='create_visitor'),
    path('api/v1/visitor/list/', VisitorViewSet.as_view({'get': 'list'}), name='list_visitor'),
    path('docs/', include_docs_urls(title='API Docs')),
]
