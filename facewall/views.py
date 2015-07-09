# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import OnlineQuestionForm
# Create your views here.
# Upload video
def index(request):
	return render(request, 'facewall/index.html', {})

def signup(request):
	form = OnlineQuestionForm(request.POST or None)

	context = {
		'title': '百人百臉投稿',
		'form': form
	}

	# check input data and clean_data success
	if form.is_valid():
		form.save()
		context = {
			'title': '恭喜您完成投稿',
			'form': form
		}

	return render(request, 'facewall/signup.html', context)