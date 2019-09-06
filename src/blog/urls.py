from django.urls import path

from .views import blog_home_view, blog_list_view, blog_create_view, blog_details_view, blog_about_view

app_name = 'blog'
urlpatterns = [
	path('home/', blog_home_view, name='blog_home_view'),
	path('list/', blog_list_view, name='blog_list_view'),
	path('create/', blog_create_view, name='blog_create_view'),
	path('details/<int:id>/', blog_details_view, name='blog_details_view'),
	path('about/', blog_about_view, name='blog_about_view')
]