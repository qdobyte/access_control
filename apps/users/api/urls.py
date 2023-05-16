from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from apps.users.api.views.home import home
from apps.users.api.views.employee import EmployeeViewSet
from apps.users.api.views.visitor import VisitorViewSet
from apps.users.api.views.employee_ingress import EmployeeIngressViewSet
from apps.users.api.views.visitor_ingress import VisitorIngressViewSet
from apps.users.api.views.report import ReportViewSet, ReportEmployeeViewSet

urlpatterns = [
    path('', home, name='home'),
    path('api/v1/employee/create/', EmployeeViewSet.as_view({'post': 'create'}), name='create_employee'),
    path('api/v1/employee/list/', EmployeeViewSet.as_view({'get': 'list'}), name='list_employee'),
    path('api/v1/visitor/create/', VisitorViewSet.as_view({'post': 'create'}), name='create_visitor'),
    path('api/v1/visitor/list/', VisitorViewSet.as_view({'get': 'list'}), name='list_visitor'),
    path('api/v1/employee/ingress/create/', EmployeeIngressViewSet.as_view({'post': 'create'}),
         name='create_ingress_employee'),
    path('api/v1/employee/ingress/update/<int:pk>/', EmployeeIngressViewSet.as_view({'put': 'update'}),
         name='update_ingress_employee'),
    path('api/v1/visitor/ingress/create/', VisitorIngressViewSet.as_view({'post': 'create'}),
         name='create_ingress_visitor'),
    path('api/v1/visitor/ingress/update/<int:pk>/', VisitorIngressViewSet.as_view({'put': 'update'}),
         name='update_ingress_visitor'),
    path('api/v1/report/list/', ReportViewSet.as_view({'get': 'list'}), name='inside_report'),
    path('api/v1/report/employee/list/', ReportEmployeeViewSet.as_view({'get': 'list'}), name='employee_report'),
    path('docs/', include_docs_urls(title='API Docs')),
]
