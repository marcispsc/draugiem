from .models import User
from draugiem import Draugiem
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def draugiem_login(request):
	d = Draugiem(settings.DRAUGIEM_ID, settings.DRAUGIEM_KEY)
	return redirect(d.get_login_url(request.build_absolute_uri(reverse('draugiem_callback'))))

def draugiem_callback(request):
	if request.GET.get('dr_auth_status') != 'ok' or not request.GET.get('dr_auth_code'):
		return HttpResponseBadRequest()
	d = Draugiem(settings.DRAUGIEM_ID, settings.DRAUGIEM_KEY)
	me = d.authorize(request.GET['dr_auth_code'])

def draugiem_logout(request):
	pass