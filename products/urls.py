from django.conf.urls import url, include
from .views import all_tickets, buy_tickets, bug, feature, full_detail

urlpatterns = [
    url(r'^$', all_tickets, name='all_tickets'),
    url(r'^buy_tickets/$', buy_tickets, name='buy_tickets'),
    url(r'^bug/$', bug, name='bug'),
    url(r'^feature/$', feature, name='feature'),
    url(r'^full_detail/$', full_detail, name='full_detail')
]
