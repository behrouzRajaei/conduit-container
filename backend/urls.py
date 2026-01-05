from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('conduit.apps.articles.urls')),
    url(r'^api/', include('conduit.apps.authentication.urls')),
    url(r'^api/', include('conduit.apps.profiles.urls')),
]

