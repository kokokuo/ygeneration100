from django.db import models

# Create your models here.
# Fast Questions
class FastQuestion(models.Model):
	description = models.TextField(blank=True, null=True)
	cover_image = models.ImageField(upload_to='upload/fast_questions')
	youtube_url = models.TextField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return u'%s' % self.id