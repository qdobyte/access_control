from django.urls import include, path
# from rest_framework import routers
from apps.users.api.views.login import signin, signup, home

# router = routers.DefaultRouter()
# router.register(r'login', signin, basename='signin')

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
]