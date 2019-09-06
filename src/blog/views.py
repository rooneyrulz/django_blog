from django.shortcuts import render


# Blog Home View
def blog_home_view(request):
	return render(request, 'blog/blog_home.html', {})


# Blog List View
def blog_list_view(request):
	return render(request, 'blog/blog_list.html', {})


# Blog Create View
def blog_create_view(request):
	return render(request, 'blog/blog_create.html', {})


# Blog Details View
def blog_details_view(request, id):
	return render(request, 'blog/blog_details.html', {'id': id})


# Blog About View
def blog_about_view(request):
	return render(request, 'blog/blog_about.html', {})
	

