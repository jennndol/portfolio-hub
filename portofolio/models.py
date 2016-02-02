from django.db import models

class Portofolio(models.Model):
	title = models.CharField(max_length=25)
	description = models.TextField(blank=True, null=True)
	image = models.FileField(upload_to='static/image')
	client = models.CharField(max_length=25, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	service = models.CharField(max_length=25, blank=True, null=True)

	def __unicode__(self):
		return self.title