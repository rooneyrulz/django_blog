from django.db import models
from django.urls import reverse
from datetime import datetime


class Blog(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	author = models.CharField(max_length=100)
	date = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:blog_details_view', kwargs={'id': self.id})
