from django.shortcuts import render
from django.http import HttpResponse


# Blog Home View
def blog_home_view(request):
	return HttpResponse('Home')


# Blog About View
def blog_about_view(request):
	return HttpResponse('About')

