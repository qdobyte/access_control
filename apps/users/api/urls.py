from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from apps.users.api.views.login import signin, signup, home
from apps.users.api.views.employee import EmployeeViewSet
from apps.users.api.views.visitor import VisitorViewSet


# router = routers.DefaultRouter()
# router.register(r'employee', EmployeeViewSet, 'employee')


urlpatterns = [
    # path('signin/', signin, name='signin'),
    # path('signup/', signup, name='signup'),
    # path('', home, name='home'),
    # path('', include(router.urls)),
    path('api/v1/employee/create', EmployeeViewSet.as_view({'post': 'create'}), name='create_employee'),
    path('api/v1/employee/update/<int:pk>', EmployeeViewSet.as_view({'put': 'update'}), name='update_employee'),
    path('api/v1/employee/delete/<int:pk>', EmployeeViewSet.as_view({'delete': 'destroy'}), name='delete_employee'),
    path('api/v1/employee/list', EmployeeViewSet.as_view({'get': 'list'}), name='list_employee'),
    path('api/v1/employee/retrieve/<int:pk>', EmployeeViewSet.as_view({'get': 'retrieve'}), name='retrieve_employee'),
    path('api/v1/visitor/create', VisitorViewSet.as_view({'post': 'create'}), name='create_visitor'),
    path('api/v1/visitor/update/<int:pk>', VisitorViewSet.as_view({'put': 'update'}), name='update_visitor'),
    path('api/v1/visitor/delete/<int:pk>', VisitorViewSet.as_view({'delete': 'destroy'}), name='delete_visitor'),
    path('api/v1/visitor/list', VisitorViewSet.as_view({'get': 'list'}), name='list_visitor'),
    path('api/v1/visitor/retrieve/<int:pk>', VisitorViewSet.as_view({'get': 'retrieve'}), name='retrieve_visitor'),

    path('docs/', include_docs_urls(title='API Docs')),
]