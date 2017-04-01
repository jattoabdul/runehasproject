from django.conf.urls import include, url
from accounts import views as accounts_views


urlpatterns = [
    url(r'^', include('userena.urls')),
    # url(r'^profile', accounts_views.profile, name='profile'),
]
