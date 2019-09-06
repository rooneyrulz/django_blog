from django.urls import path

from .views import blog_home_view, blog_about_view

app_name = 'blog'
urlpatterns = [
	path('', blog_home_view, name='blog_home_view'),
	path('about/', blog_about_view, name='blog_about_view')
]