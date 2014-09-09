from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', 'sums_squares.views.home', name='home'),
    url(r'^difference', 'sums_squares.views.difference', name='difference'),
)
