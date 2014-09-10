from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^difference', 'sums_squares.views.difference', name='difference'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
