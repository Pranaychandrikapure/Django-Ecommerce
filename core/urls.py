from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('category/', category_list_view, name='category-list'),
    path('products/', product_list_view, name='product-list'),
    path('category/<cid>/', category_product_list_view, name='category-product-list'),
    path('vendor/',vendor_list_view,name='vendor-list'),
    path('vendor/<vid>/',vendor_details_view,name='vendor-detail-view'),
    path('product/<pid>/',product_details_view,name='product-details'),
    path('products/tag/<slug:tag_slug>/',tag_list,name='tags'),
    path('ajax-add-review/<int:pid>/',ajax_add_review,name='ajax-add-review'),
    path('search/', search_view, name='search'),
    path('filter-products/', filter_product, name='filter-product'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
]

