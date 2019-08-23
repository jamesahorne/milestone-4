from django.conf.urls import url, include
from django.contrib import admin
from home import urls as home_urls
from accounts import urls as accounts_urls
from products import urls as products_urls
from django.views import static
from .settings.base import MEDIA_ROOT
from cart import urls as cart_urls
from search import urls as search_urls
from checkout import urls as checkout_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^tickets/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(checkout_urls))
]
