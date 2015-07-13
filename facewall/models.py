# -*- coding: utf-8 -*-
from django.db import models

# 重新命名檔案名稱
# def generate_new_filename(instance, filename):
# 	return 'upload/picture_story/' + 'article' + "_" + filename

# Create your models here.
class OnlineQuestion(models.Model):

	name = models.CharField(max_length=20, blank=False, null=False)
	nickname = models.CharField(max_length=20, blank=False, null=False)

	# 如果要連結到Radio, 指定布林值對應的選擇，如果預設是不選，則設定default = None
	gender = models.BooleanField(
		default=None,
		null=False,
		choices=((True, '男性'), (False, '女性'))
	)

	birth_year = models.IntegerField(
		max_length=4,
		default=None, blank=False, null=False,
		choices=[(i, i) for i in range(1910, 2020)]
	)
	birth_month = models.IntegerField(
		max_length=2,
		default=None, blank=False, null=False,
		choices=[(i, i) for i in range(1, 13)]
	)
	birth_day = models.IntegerField(
		max_length=2,
		default=None, blank=False, null=False,
		choices=[(i, i) for i in range(1, 32)]
	)

	contact_email = models.EmailField()
	content = models.TextField(blank=True, null=True)
	face_image = models.ImageField(
		upload_to='upload/picture_story/'
	)
	youtube_url = models.URLField(blank=False, null=False)
	# 主題
	topic_num = models.CharField(max_length=10, blank=False, null=False)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return u'%s %s' % (self.id, self.name)