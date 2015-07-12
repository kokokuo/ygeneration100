# -*- coding: utf-8 -*-
from django import forms
from .models import OnlineQuestion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Fieldset, Div, MultiField, Submit
from crispy_forms.bootstrap import AppendedText
import re

class OnlineQuestionForm(forms.ModelForm):
	class Meta:
		model = OnlineQuestion
		# Show field on th form
		fields = [
			'name', 'nickname', 'gender',
			'birth_year','birth_month','birth_day',
			'contact_email','face_image',
			'content', 'youtube_url', 'topic_num']

		labels = {
			'name': '姓名',
			'nickname': '暱稱',
			'gender': '性別',
			'birth_year': '出生年',
			'birth_month': '出生月',
			'birth_day': '出生日',
			'contact_email': '連絡信箱',
			'content': '介紹',
			'face_image': '大頭貼',
			'youtube_url': 'Youtube 影片連結',
			'topic_num': '投稿題目'
		}
		widgets = {
			'gender': forms.RadioSelect(attrs={'style':'margin-left:40px;'}),
			'topic_num': forms.Select(
				choices=[
				# 前面是值後面是顯示
				('Ques1', '如果外國人來台灣，會帶他去哪邊玩？'),
				('Ques2', '在機場發生的奇聞軼事或有趣/麻煩事件'),
				('Ques3','在機場都消費什麼？'), ('Ques4','最喜歡的異國文化？'), ('Ques5','對你來說什麼是小確幸')]
			),
		}

	def __init__(self, *args, **kwargs):
		super(OnlineQuestionForm,self).__init__(*args, **kwargs)
 		# Set layout for fields.
 		self.helper = FormHelper()
 		# 用 FieldSet切群組
 		self.helper.layout = Layout(
 			Fieldset(
 				# u'基本資料',
 				'',
 				Div(
	        		Div('name',css_class="col-md-4"),
	        		css_class="row"
	        	),
	        	Div(
	        		Div('nickname',css_class="col-md-4"),
	        		css_class="row"
        		),
        		Div(
        			Div('contact_email',css_class="col-md-6"),
        			css_class="row"	
    			),
    		),
    		Div('gender'),
    		Fieldset(
    			# u'生日',
    			'',
 				Div(
	        		Div('birth_year',css_class="col-md-4"),
	        		Div('birth_month',css_class="col-md-4"),
	        		Div('birth_day',css_class="col-md-4"),
	        		css_class="row"
	        	)
	        	
    		),
        	'face_image',
			'content', 
			'youtube_url', 
			'topic_num'
		)
		# 用index指令layout的區塊
		self.helper[0].wrap_together(Fieldset, u'基本資料',style="font-weight: bold;")
		self.helper[3:7].wrap_together(Fieldset, u'投稿資料',style="font-weight: bold;")
		# 客製化的按鈕
 		# self.helper.add_input(Submit('submit', 'Submit'))


	def clean_name(self):
		name = self.cleaned_data.get('name')
		# 特別符號，待處理
		return name

	# def clean_face_image(self):
	# 	face_image = self.cleaned_data.get('face_image')
	# 	image_w, image_h = face_image.size
	# 	if image_w > 300 or image_h > 300:
	# 		face_image.resize((300, 300), Image.ANTIALIAS)
	# 	return face_image

	def clean_youtube_url(self):
		url = self.cleaned_data.get('youtube_url')
		match_pattern = '^http[s]://www.youtube.com/'
		matched = re.search(match_pattern, url)
		if not matched:
			raise forms.ValidationError('不是有效的Youtube連結')
		return url
