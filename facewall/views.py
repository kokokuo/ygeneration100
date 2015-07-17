# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import OnlineQuestionForm
from .models import OnlineQuestion
# Create your views here.
# 索引頁
def index(request):
	return render(request, 'facewall/index.html', {})

def add(request):
	# 一開始透過None 表示為空白表單
	form = OnlineQuestionForm(None)
	# 如果為Post新建一個表單，並指定request.FILES 表示表單有檔案，使得檔案被上傳成功，
	if request.method == 'POST':
		form = OnlineQuestionForm(request.POST, request.FILES)
		# check input data and clean_data success
		if form.is_valid():
			saved_inst = form.save()
			# 取得儲存的 model
			online_ques_model = OnlineQuestion.objects.get(pk=saved_inst.pk)
			# Send Email , 通知有新增投稿使用者
			submit_name = online_ques_model.name
			submit_gender = u'男性' if online_ques_model.gender is True else u'女性'
			submit_birthday = str(online_ques_model.birth_year) +  \
				'/' + str(online_ques_model.birth_month) + \
				'/' + str(online_ques_model.birth_day)
			submit_email = online_ques_model.contact_email
			submit_face_image = online_ques_model.face_image.url
			submit_youtube = online_ques_model.youtube_url
			submit_topic = online_ques_model.topic_num

			mail_topic = u'百人百臉，新投稿資料，投稿人:' + submit_name

			messgae = u'姓名:' + submit_name + '\n' + \
				u'性別:' + submit_gender + '\n' + \
				u'生日:' + submit_birthday + '\n' + \
				u'信箱:' + submit_email + '\n' + \
				u'大頭照:' + submit_face_image + '\n' + \
				u'Youtube連結:' + submit_youtube + '\n' + \
				u'選擇題目:' + submit_topic

			to_list = [
				'bepci2015@gmail.com',
				'john01311@gmail.com',
				'l502227ina@gmail.com'
			]
			# Send Email STMP
			send_mail(
				mail_topic,
				messgae,
				settings.EMAIL_HOST_USER, to_list,
				fail_silently=False)

			context = {
				'title': '恭喜您完成投稿',
				'name': form.cleaned_data.get('name')
			}
			return render(request, 'facewall/result.html', context)
	context = {
		'title': '百人百臉投稿',
		'onlineform': form
	}
	return render(request, 'facewall/add.html', context)