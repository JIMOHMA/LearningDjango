from django.urls import path
from .views import (
    product_detail_view, 
    product_create_view, 
    product_update_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    )


app_name = 'products'
urlpatterns = [
	
    # This is the part for dynamic URL
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('detail/', product_detail_view, name='product-detail'),
    path('<int:my_id>/', dynamic_lookup_view, name='product-lookup'), #dynamic way instead of static way above
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
    path('<int:my_id>/update/', product_update_view, name='product-update'),
]