from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

def home(request):
    return HttpResponse("Backend is running")

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include('conduit.apps.authentication.urls')),
    url(r'^api/', include('conduit.apps.profiles.urls')),
    url(r'^api/', include('conduit.apps.articles.urls')),
]
