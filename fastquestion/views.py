# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import FastQuestion
from facewall.models import OnlineQuestion
# finder real static path
from django.contrib.staticfiles import finders
# file search
from os import listdir
from random import shuffle
from django.http import HttpResponse
import json
# Regex
import re

online_ques_list = list(OnlineQuestion.objects.all())
# Create your views here.
# Fast Question Wall
def index(request):

	# 取得投稿的圖片與連結
	# # 把資料放到list , QuerySet無法被更改
	shuffle(online_ques_list)
	# # 取得上傳至後台的快問快答影片與連結
	# # 把資料放到list , QuerySet無法被更改
	# fast_ques_list = list(FastQuestion.objects.all())
	# shuffle(fast_ques_list)
	# top_twenty_online_data = list(fast_ques_list[:20])
	# real_static_path = finders.find('images/fast_question/')
	# files = [f for f in listdir(real_static_path)]
	# static_files = ['images/fast_question/' + f for f in files]
	# shuffle(static_files)

	context = {
		# 'fast_ques_list': fast_ques_list,
		'online_facewall': list(online_ques_list[:40]),
		'online_ques_list': list(online_ques_list)
	}
	return render(request, 'fastquestion/index.html', context)

def get_face_video(request):
	# Ajax get
	if request.method == 'GET':
		face_id = int(request.GET['face_id'])
		select_m = OnlineQuestion.objects.get(pk=face_id)

		# youtube link handle
		match_pattern = 'v=[a-zA-Z0-9_]]+&*'
		url = select_m.youtube_url
		matched = re.search(match_pattern, url)
		# Get Matched data
		youtube_raw_serial = matched.group()
		if '&' in youtube_raw_serial:
			youtube_serial = youtube_raw_serial[2:-1]
		else:
			youtube_serial = youtube_raw_serial[2:]

		# name and nickname
		title = None
		content = None
		if not select_m.nickname:
			title = select_m.nickname
		else:
			title = select_m.name

		content = select_m.content
		# message

		message = {
			'youtube_serial': youtube_serial,
			'title': title,
			'content': content
		}
		json_data = json.dumps(message)
		return HttpResponse(json_data, content_type='application/json')
	return HttpResponse('')