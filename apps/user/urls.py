from django.conf.urls import url
from user import views
from user.views import RegisterView

urlpatterns = [
    url(r'^register$', views.register, name='register'),  # 注册
    url(r'^register_handle$', views.register_handle, name='register_handle'),  # 注册
    url(r'^reg/$', RegisterView.as_view(), name='reg'),
]
