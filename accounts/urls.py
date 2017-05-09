from django.conf.urls import include, url
from accounts import views as accounts_views
from django.contrib.sites.models import Site


urlpatterns = [
    url(r'^', include('userena.urls')),
    # url(r'^profile', accounts_views.profile, name='profile'),
]
