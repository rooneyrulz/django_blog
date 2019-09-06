from django.shortcuts import render


# Blog Home View
def blog_home_view(request):
	return render(request, 'blog/blog_home.html', {})


# Blog About View
def blog_about_view(request):
	return render(request, 'blog/blog_about.html', {})
	

