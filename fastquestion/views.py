# -*- coding: utf-8 -*-
from django.shortcuts import render
from facewall.models import OnlineQuestion
from random import shuffle
from django.http import HttpResponse
import json
# Regex
import re

# Create your views here.
# Fast Question Wall
def index(request):
	# 取得投稿的圖片與連結
	# 把資料放到list , QuerySet無法被更改
	online_ques_list = list(OnlineQuestion.objects.all())

	shuffle(online_ques_list)

	context = {
		# 'fast_ques_list': fast_ques_list,
		'online_facewall': list(online_ques_list[:40]),
		'online_ques_list': list(online_ques_list[:15]),
		'page_id': 1
	}
	return render(request, 'fastquestion/index.html', context)

def get_face_video(request):
	# Ajax get
	if request.method == 'GET':
		face_id = int(request.GET['face_id'])
		select_m = OnlineQuestion.objects.get(pk=face_id)

		# youtube link handle
		match_pattern = 'v=[a-zA-Z0-9_\-]+&*'
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
		if select_m.nickname:
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

# 待修改
def get_page(request, page_id):
	# 取得投稿的圖片與連結
	# 把資料放到list , QuerySet無法被更改
	online_ques_list = list(OnlineQuestion.objects.all())
	# 打亂資料
	shuffle(online_ques_list)
	# 分配抓取 每次抓取15筆
	start_num = (int(page_id) - 1) * 15
	last_num = int(page_id) * 15
	context = {
		'online_ques_list': online_ques_list[start_num:last_num],
		'page_id': int(page_id) + 1
	}

	return render(request, 'fastquestion/index.html', context)