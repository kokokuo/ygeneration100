# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import FastQuestion
from facewall.models import OnlineQuestion
# finder real static path
from django.contrib.staticfiles import finders
# file search
from os import listdir
from random import shuffle

# Create your views here.
# Fast Question Wall
def index(request):

	# 取得投稿的圖片與連結
	# 把資料放到list , QuerySet無法被更改
	online_ques_list = list(OnlineQuestion.objects.all())
	shuffle(online_ques_list)
	# 取得上傳至後台的快問快答影片與連結
	# 把資料放到list , QuerySet無法被更改
	fast_ques_list = list(FastQuestion.objects.all())
	shuffle(fast_ques_list)

	# real_static_path = finders.find('images/fast_question/')
	# files = [f for f in listdir(real_static_path)]
	# static_files = ['images/fast_question/' + f for f in files]
	# shuffle(static_files)

	context = {
		'fast_ques_list': fast_ques_list[:20],
		'online_ques_list': online_ques_list
	}
	return render(request, 'fastquestion/index.html', context)