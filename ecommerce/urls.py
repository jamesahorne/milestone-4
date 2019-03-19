from django.conf.urls import url
from django.contrib import admin
from accounts.views import index, logout, login, registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/registration/$', registration, name="registration")
]
