from django.conf.urls import url, include
from accounts.views import logout, login, registration, profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', registration, name="registration"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
