from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm


# This is the first method showed on how to create a product form 
# with django
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# This is how we can set initial data to a form
def product_initial_data(request):
	initial_data = {
		'title': 'This is an awesome title'
	}
	obj = Product.objects.get(id=4)
	form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)


# Building django form from scratch 
# def product_create_view(request):

# 	#this is request.GET by default
# 	my_form = RawProductForm() 
# 	if request.method == 'POST':

# 		#this validates our entry forms
# 		my_form = RawProductForm(request.POST) 

# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			# now the data is good
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		'form': my_form
# 	}
# 	return render(request, "products/product_create.html", context)


# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)



