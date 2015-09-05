# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def home(request):
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