from django.conf.urls import url, include

urlpatterns = [
    url(r'^member/', include('member.urls')),
    url(r'^post/', include('post.urls')),
]