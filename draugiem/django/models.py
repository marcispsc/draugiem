from django.db import models

class User(models.Model):
	GENDER_CHOICES = (
		('M', u'Male',),
		('F', u'Female',),
	)

	uid = models.IntegerField(unique=True)
	apikey = models.CharField(max_length=23)
	language = models.CharField(max_length=2)
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	nick = models.CharField(max_length=100, blank=True)
	age = models.PositiveSmallIntegerField()
	adult = models.BooleanField()
	image = models.ImageField(upload_to='draugiem')
	gender = models.CharField(choices=GENDER_CHOICES)

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u'%s %s' % (self.name, self.surname,)

	def get_profile_link(self):
		return u'http://www.draugiem.lv/user/%d/' % self.uid