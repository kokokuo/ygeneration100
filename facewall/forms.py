# -*- coding: utf-8 -*-
from django import forms
from .models import OnlineQuestion
import re

class OnlineQuestionForm(forms.ModelForm):
	class Meta:
		model = OnlineQuestion
		# Show field on th form
		fields = ['name', 'contact_email', 'content', 'face_image', 'youtube_url']
		labels = {
			'name': '名稱',
			'contact_email': '連絡信箱',
			'content': '介紹',
			'face_image': '大頭貼',
			'youtube_url': 'Youtube 影片連結'
		}

	def clean_name(self):
		name = self.cleaned_data.get('name')
		# 特別符號，待處理
		return name

	def clean_youtube_url(self):
		url = self.cleaned_data.get('youtube_url')
		match_pattern = '^http[s]://www.youtube.com/'
		matched = re.search(match_pattern, url)
		if not matched:
			raise forms.ValidationError('不是有效的Youtube連結')
		return url
