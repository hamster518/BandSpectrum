from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.band_search, name='band_search'),
]