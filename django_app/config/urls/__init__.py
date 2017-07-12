from django.conf.urls import include
from django.conf.urls import url
from . import urls_view, urls_apis
urlpatterns = [
    url(r'', include(urls_view)),
    url(r'^apis/', include(urls_apis))
]