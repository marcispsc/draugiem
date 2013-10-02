Draugiem
========

Python wrapper for draugiem.lv API

Features
--------

* Authentification
* API V4 and V5 support

Installation
------------

Install via [pip](http://www.pip-installer.org/)

	pip install pip install git+git://github.com/BUHARDI/draugiem.git

Or, if you want the code that is currently on GitHub

	git clone git://github.com/BUHARDI/draugiem.git

Starting Out
------------

Register an application http://www.draugiem.lv/applications/dev/create/

After you have registered the application, copy and save ID and API KEY. Example below shows that I have stored those variables in Django settings as DRAUGIEM_ID and DRAUGIEM_KEY.

Now you're ready to use draugiem.lv API. Import the wrapper class.

	from draugiem import Draugiem

Authentification
----------------

> This example is based on [Django framework](https://www.djangoproject.com/)

Example shows how to get draugiem.lv user data. You only need to do this, if you created an application of type "passport application".

Typically this would be the process starting view.

	from django.conf import settings

	def login_draugiem(request):
		draugiem = Draugiem(settings.DRAUGIEM_ID, settings.DRAUGIEM_KEY)
		callback_url = 'http://domain.tld/login/draugiem/callback'
		login_url = draugiem.get_login_url(callback_url)
		return redirect(login_url)

`callback_url` is url where user will be redirected after login on draugiem.lv. In this view you will receive extra GET variables to complete the autorization.

Last things to end the login process - callback view. Documentation: [latvian](http://www.draugiem.lv/applications/dev/docs/passport/#lietotaja-autorizacija-un-profila-informacijas-iegusana-pieprasijums-authorize), [english](http://www.draugiem.lv/applications/dev/docs/passport_en/#user-authentication-process-request-authorize).

	def login_draugiem_callback(request):
		if request.GET.get('dr_auth_status') != 'ok' or not request.GET.get('dr_auth_code'):
		    return HttpResponseBadRequest()
		draugiem = Draugiem(settings.DRAUGIEM_ID, settings.DRAUGIEM_KEY)
		user = draugiem.authorize(request.GET['dr_auth_code'])

Thats it! `user` variable contains dictionary of user profile.

To use API as user that just authorized, you have to set user API KEY.

	draugiem.set_apikey(user['apikey'])

It's good idea store the user API KEY in case you want use API again later. In Django you can take advantage of sessions.

	request.session['draugiem_apikey'] = user['apikey']

Using the API
-------------

Chekout the code and the documentation ([latvian](http://www.draugiem.lv/applications/dev/docs/passport/#pieejamie-api-pieprasijumi), [english](http://www.draugiem.lv/applications/dev/docs/passport_en/#available-api-requests)). You should be ready to dive in by now.

	draugiem = Draugiem(settings.DRAUGIEM_ID, settings.DRAUGIEM_KEY, request.session['draugiem_apikey'])

Create an instance. Third argument is user API KEY which you received after user authorization.

More examples:

	userdata = draugiem.api('userdata', ids='1,2,3') # getting user data of specific users

	users = draugiem.api('app_users') # getting list of application users

	draugiem.api('add_activity', prefix='ate', text='banana')

API V5
------

This is secret feature for undocumented part of draugiem.lv API. Use this on your own risk!

	messages = draugiem.api('app_messages', 'POST')

	transaction = draugiem.api('app_transactionCreate', 'POST', price=0, service='test')

	say_post = draugiem.api('say_post', 'POST',
	    poster_type = 0,
	    text = 'Post text',
	    prefix = 'Prefix',
	    link = 'http://dra.lv/m5',
	    title = 'Title text',
	    pic_content = '',
	    uid = 100774,
	)