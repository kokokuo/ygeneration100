# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import OnlineQuestionForm
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
			form.save()
			context = {
				'title': '恭喜您完成投稿',
				'name': form.cleaned_data.get('name')
			}
			return render(request, 'facewall/result.html', context)
	context = {
		'title': '百人百臉投稿',
		'form': form
	}
	return render(request, 'facewall/add.html', context)