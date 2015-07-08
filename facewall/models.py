from django.db import models

# Create your models here.
class OnlineQuestion(models.Model):
	name = models.CharField(max_length=20, blank=False, null=False)
	contact_email = models.EmailField()
	content = models.TextField(blank=True, null=True)
	face_image = models.ImageField(upload_to='upload/picture_story/')
	youtube_url = models.TextField(blank=False, null=False)
	type = models.CharField(max_length=10, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return u'%s %s' % (self.id, self.name)