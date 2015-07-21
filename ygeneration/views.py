# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# finder real static path
from django.contrib.staticfiles import finders
# file search
from os import listdir
from random import shuffle

# Create your views here.
def home(request):
	# real_static_path = finders.find('images/fast_question/')
	# files = [f for f in listdir(real_static_path)]
	# static_files = ['images/fast_question/' + f for f in files]
	# # 亂數排序
	# shuffle(static_files)
	# context = {
	# 	'fast_ques_photo': static_files,
	# }
	return render(request, 'home.html', {})

def activity_intro(request):
	return render(request, 'activity_intro.html', {})


def team_intro(request):
	return render(request, 'team_intro.html', {})


def error404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response
def error500(request):
	response = render_to_response('500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response