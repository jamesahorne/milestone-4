from django.conf.urls import url
from .views import index, about, data, DataVisualisation # ,get_data


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name="about"),
    url(r'^data/$', data, name="data"),
#    url(r'^api/data/$', get_data, name="get_data"),
    url(r'^api/graphs/data/$', DataVisualisation.as_view())
]
