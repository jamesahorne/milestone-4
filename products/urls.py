from django.conf.urls import url, include
from .views import all_tickets, buy_tickets, bug, feature, full_detail, feature_or_upvote, upvote, add_upvote

urlpatterns = [
    url(r'^$', all_tickets, name='all_tickets'),
    url(r'^buy-tickets/$', buy_tickets, name='buy_tickets'),
    url(r'^bug/$', bug, name='bug'),
    url(r'^feature/$', feature, name='feature'),
    url(r'^full-detail/(?P<pk>\d+)$', full_detail, name='full_detail'),
    url(r'^feature-or-upvote/$', feature_or_upvote, name='feature_or_upvote'),
    url(r'^upvote/$', upvote, name='upvote'),
    url(r'^add-upvote/(?P<pk>\d+)$', add_upvote, name='add_upvote')
]
