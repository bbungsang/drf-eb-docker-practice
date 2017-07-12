from django.conf.urls import url

from member import views
from member.views import UserListCreateView

urlpatterns = [
    url(r'^user/$', UserListCreateView.as_view()),

    # 반드시 pk 로, user_pk 혹은 post_pk 와 같은 다른 기본키 이름은 안 됨.
    url(r'(?P<pk>\d+)/$', views.UserRetrieveUpdateDestroyView.as_view())
]