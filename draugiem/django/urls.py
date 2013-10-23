from django.conf.urls.defaults import *

urlpatterns = patterns('draugiem.django.views',
	url(r'^login$', 'draugiem_login'),
	url(r'^login/callback$', 'draugiem_callback'),
	url(r'^logout$', 'draugiem_logout'),
)