#from django.conf.urls import url
#
#from .views import(
#    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView)
#
#urlpatterns = [
#    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
#    url(r'^users/?$', RegistrationAPIView.as_view()),
#    url(r'^users/login/?$', LoginAPIView.as_view()),
#]


from django.conf.urls import url
from .views import (
    LoginAPIView, 
    RegistrationAPIView, 
    UserRetrieveUpdateAPIView
)

# Define app_name for namespacing
app_name = 'authentication'

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    url(r'^users/?$', RegistrationAPIView.as_view(), name='user-register'),
    url(r'^users/login/?$', LoginAPIView.as_view(), name='user-login'),
]

