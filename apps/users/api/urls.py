from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from apps.users.api.views.login import signin, signup, home
from apps.users.api.views.employee import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet, 'employee')

urlpatterns = [
    # path('signin/', signin, name='signin'),
    # path('signup/', signup, name='signup'),
    # path('', home, name='home'),
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='API Docs')),
]