# -*- coding: utf-8 -*-
from django import forms

from .models import OnlineQuestion
# Crispy form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Fieldset, Div, MultiField, Submit
from crispy_forms.bootstrap import AppendedText
# For Image
from django.conf import settings
import StringIO
from PIL import Image
# Regex
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
		# 設定協助描述的文字
		help_texts = {
			'face_image': '請上傳寬 * 高為640 x 640以下的圖檔',
			'youtube_url': '請記得公開影片, 並提供連結即可, 不需提供分享影片程式碼',
		}

		widgets = {
			'gender': forms.RadioSelect(attrs={'style': 'margin-left:40px;'}),
			'topic_num': forms.Select(
				choices=[
					# 前面是值後面是顯示
					('Ques1', 'Q1:你最喜歡的國家是哪個國家呢? 如果有機會可以待在國外生活，你會選擇待在國外還是留在台灣? 為什麼?'),
					('Ques2', 'Q2:假設你的外國朋友來台灣，你會想帶他去哪裡玩?有沒有一件事是一定要在那邊做的?為什麼?'),
					('Ques3', 'Q3:現今大家都說台灣人喜愛小確幸，那你會怎麼定義小確幸這個詞，如果你覺得小確幸是一件好事，那小確幸對生活帶來什麼助益? 如果你覺得小確幸不好，原因又是什麼?'), 
					('Ques4', 'Q4:每個人或多或少都有過出國的經驗，而出國及歸國時我們都會踏入機場，有沒有什麼經驗是讓你覺得出國前和歸國後的心態有明顯轉變的? 為什麼?')
				]
			),
		}

	def __init__(self, *args, **kwargs):
		super(OnlineQuestionForm, self).__init__(*args, **kwargs)
 		# Set layout for fields.
 		self.helper = FormHelper()

 	# 	# 設定名稱，另一種方式，第三個是描述
		# online_question_field_text = [
		# 	# (field_name, Field title label, Detailed field description)
		# 	('name', '姓名', ''),
		# 	('nickname', '暱稱', ''),
		# 	('gender', '性別', ''),
		# 	('birth_year', '出生年', ''),
		# 	('birth_month', '出生月', ''),
		# 	('birth_day', '出生日', ''),
		# 	('contact_email', '連絡信箱', ''),
		# 	('content', '介紹', ''),
		# 	('face_image', '大頭貼', '請上傳300Kb以下的圖檔'),
		# 	('youtube_url', 'Youtube 影片連結', '請記得公開影片, 並提供連結即可, 不需提供分享影片程式碼'),
		# 	('topic_num', '投稿題目', '')
		# ]

		# for x in online_question_field_text:
		# 	self.fields[x[0]].label=x[1]
		# 	self.fields[x[0]].help_text=x[2]

 		# 客製化layout排版 用 FieldSet切群組
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
		# 群組
		self.helper[0].wrap_together(Fieldset, u'基本資料',style="font-weight: bold;")
		self.helper[3:7].wrap_together(Fieldset, u'投稿資料',style="font-weight: bold;")
		# 客製化的按鈕
 		self.helper.add_input(Submit('submit', u'投稿',css_class="btn btn-success signup_btn"))


	def clean_name(self):
		name = self.cleaned_data.get('name')
		# 特別符號，待處理
		return name

	def clean_face_image(self):
		face_image = self.cleaned_data.get('face_image')
		if face_image:
			face_image_file = StringIO.StringIO(face_image.read())
			image = Image.open(face_image_file)
			w, h = image.size
			if not image.format in settings.VALID_IMAGE_FORMATS:
				raise forms.ValidationError(u'只有 *.bmp, *.jpg 與 *.png 圖片格式允許上傳')
			if w > settings.VALID_IMAGE_WIDTH or h > settings.VALID_IMAGE_HEIGHT:
				raise forms.ValidationError(u'圖片尺寸不符，影像寬超出' + str(settings.VALID_IMAGE_WIDTH) + u'像素,或是高' + str(settings.VALID_IMAGE_HEIGHT) + u'像素.')
			#  Rename File
		return face_image

	def clean_youtube_url(self):
		url = self.cleaned_data.get('youtube_url')
		match_pattern = '^http[s]://www.youtube.com/'
		matched = re.search(match_pattern, url)
		if not matched:
			raise forms.ValidationError('不是有效的Youtube連結')
		return url
