from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'tile',
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter title'
			}
		)
	)

	description = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'id': 'description',
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter description',
				'rows': 4
			}
		)
	)

	author = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'author',
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter author'
			}
		)
	)

	# date = forms.DateTimeField(
	# 	widget=forms.DateTimeField(
	# 		attrs={
	# 			'id': 'date',
	# 			'class': 'form-control form-control-lg'
	# 		}
	# 	)
	# )

	class Meta:
		model = Blog
		fields = [
			'title',
			'description',
			'author',
			'date'
		]