from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog
from .forms import BlogForm


# Redirect to Home View
def redirect_to_home_view(request):
	return redirect('/blog/home')


# Blog Home View
def blog_home_view(request):
	return render(request, 'blog/blog_home.html', {})


# Blog List View
def blog_list_view(request):
	blog_list = Blog.objects.all()
	context = {
		'blog_list': blog_list
	}
	return render(request, 'blog/blog_list.html', context)


# Blog Create View
def blog_create_view(request):
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = BlogForm()

	context = {
	'form': form
	}
	return render(request, 'blog/blog_create.html', context)


# Blog Details View
def blog_details_view(request, id):
	blog_object = get_object_or_404(Blog, id=id)
	context = {
		'blog_object': blog_object
	}
	return render(request, 'blog/blog_details.html', context)


# Blog About View
def blog_about_view(request):
	return render(request, 'blog/blog_about.html', {})
	

