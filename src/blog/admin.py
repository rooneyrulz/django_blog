from django.contrib import admin

from .models import Blog

admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog Admin Area'
admin.site.index_title = 'Welcome to Blog Admin Area'

admin.site.register(Blog)