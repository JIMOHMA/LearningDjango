from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								widget=forms.TextInput(
										attrs={
											'placeholder': "Your Title"
										}
									)
								) 
	content = 	forms.CharField(required=False,
							widget=forms.Textarea(
									attrs={
										'placeholder': "Your Description",
										'class': 'new-class-name two',
										'id': 'my-id-for-textarea',
										'rows': 20,
										'cols': 120
									}
								)
							)
	class Meta:
		model = Article
		# This is how you include all the attributes from the Article class
		fields = ['title', 'content']
		# fields = __all__

			

class RawProductForm(forms.Form):
	pass