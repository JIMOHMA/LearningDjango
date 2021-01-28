from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Product
from .forms import ProductForm, RawProductForm


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

# Method to update the details of a products
def product_update_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# This is how we can set initial data to a form
def product_initial_data(request):
	initial_data = {
		'title': 'This is an awesome title'
	}
	obj = Product.objects.get(id=8)
	form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
	# This allows us to not add an initial data into the title field
	formNoInitialData = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=8)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, my_id):
	# One-liner for the block of comment below
	# instead of using DoesNotExist
	obj = get_object_or_404(Product, id=my_id)

	# Adding a valid error page to catch non-existent item in our database 
	try:
		obj_1 = Product.objects.get(id=my_id)
		print(obj_1.title, obj_1.description, obj_1.price)
	except Product.DoesNotExist:
		raise Http404
		
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):

	# One-liner for the block of comment below
	obj = get_object_or_404(Product, id=my_id)

	# POST request for deleting an item from the database
	# This renders a confirm option
	# On the other hand, GET request deletes instantly which 
	# can be detremental to a degree
	if request.method == 'POST':
		obj.delete() # happens on a GET request
		return redirect('../')
	context = {
		'object': obj
	}
	return render(request, "products/product_delete.html", context)


def product_list_view(request):
	queryset = Product.objects.all() # returns a list of objects
	context = {
		'object_list': queryset,
	}
	return render(request, "products/product_list.html", context)