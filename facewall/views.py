# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import OnlineQuestionForm
# Create your views here.
# Upload video
def index(request):
	return render(request, 'facewall/index.html', {})

def add(request):
	# 需要透過post or None來使得表單驗證失敗時，可以顯示錯誤訊息
	# request.FILES 表示表單有檔案使得檔案被上傳成功，

	form = OnlineQuestionForm(request.POST or None, request.FILES)
	if request.method == 'POST':
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