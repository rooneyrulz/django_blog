from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog
from .forms import BlogForm


# Redirect to Home View
def redirect_to_home_view(request):
	return redirect('/blog/home')


# Blog Home View
def blog_home_view(request):
	context = {
		'title': 'Home'
	}
	return render(request, 'blog/blog_home.html', context)


# Blog List View
def blog_list_view(request):
	blog_list = Blog.objects.all()
	context = {
		'title': 'List',
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
		'title': 'Create',
		'form': form
	}
	return render(request, 'blog/blog_create.html', context)


# Blog Details View
def blog_details_view(request, id):
	blog_object = get_object_or_404(Blog, id=id)
	context = {
		'title': 'Details',
		'blog_object': blog_object
	}
	return render(request, 'blog/blog_details.html', context)


# Blog Edit View
def blog_edit_view(request, id):
	blog_object = get_object_or_404(Blog, id=id)
	form = BlogForm(request.POST or None, instance=blog_object)
	if form.is_valid():
		form.save()
		return redirect(f'/blog/details/{id}')
	context = {
		'title': 'Edit',
		'form': form
	}
	return render(request, 'blog/blog_edit.html', context)


# Blog About View
def blog_about_view(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/blog_about.html', context)
	

