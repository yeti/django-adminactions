from django.conf.urls import patterns, url
from views import format_date


urlpatterns = patterns('',
                       url(r'^s/format/date/$', format_date, name='adminactions.format_date'))
