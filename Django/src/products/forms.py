from django import forms

from .models import Product 

class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								widget=forms.TextInput(
										attrs={
											'placeholder': "Your Title"
										}
									)
								) 
	email 		= forms.EmailField()
	description = forms.CharField(required=False,
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
	price 		= forms.DecimalField(initial=199.99)
	class Meta:
		model = Product
		fields = ['title', 'description', 'price']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		print(title)
		if not 'CFE' in title:
			raise forms.ValidationError("This is not a valid title 1!")
		elif not 'ayo' in title:
			raise forms.ValidationError("This is not a valid title 2!")
		elif not 'bola' in title:
			raise forms.ValidationError("This is not a valid title for bola!")
		else:
			return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if not email.endswith('edu'):
			raise forms.ValidationError("This is not a valid email!")
		return email
			

class RawProductForm(forms.Form):
	# label = '' # makes the label not appear
	title 		= forms.CharField(label='', 
								widget=forms.TextInput(
										attrs={
											'placeholder': "Your Title"
										}
									)
								) 
	description = forms.CharField(required=False,
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
	price 		= forms.DecimalField(initial=199.99)