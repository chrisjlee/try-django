from django.conf.urls.defaults import *
from myproject.views import hello, current_datetime, hours_ahead, chapter_request

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^status/$', chapter_request),
)
