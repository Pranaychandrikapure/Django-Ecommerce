from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from core.models import *
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from core.forms import ProductReviewForm
from django.http import JsonResponse
# from django.db.models import Q
from fuzzysearch import find_near_matches
from django.template.loader import render_to_string
from django.contrib.sessions.models import Session


#--------display products------------
def index(request):
    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(featured=True,product_status="published").order_by('-id')
    categories = Category.objects.all().order_by('-id')
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'core/index.html',context)

#-----display all ctegroy-------
def category_list_view(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories
    }
    return render(request, 'core/category-list.html', context)

#-------- prodcut list view --------
def product_list_view(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'core/product-list.html', context)

#--------- making catrgory of products ---------
def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category,product_status="published").order_by('-id')
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'core/category-product-list.html', context)


#------------ Vendor ---------------------
def vendor_list_view(request):
    vendor = Vendor.objects.all()
    context = {
        'vendor':vendor,
    }
    return render(request , "core/vendor-list.html",context)

#------------- Vendor Details page ----------------
def vendor_details_view(request,vid):
    vendor = Vendor.objects.get(vid = vid)
    products = Product.objects.filter(vendor=vendor,product_status="published").order_by('-id')
    category = Category.objects.all()
    context = {
        'vendor':vendor,
        'products':products,
        'categories':category,
    }
    return render(request,"core/vendor-details.html",context)


#------------- Prduct details page ---------------
def product_details_view(request,pid):
    product = Product.objects.get(pid = pid)
    p_images = product.p_images.all()
    # address = Address.objects.get(user=request.user)
    products = Product.objects.filter(category= product.category)
    all_products = Product.objects.all().order_by('-id')
    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    review_form = ProductReviewForm()
    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()
        if user_review_count > 0:
            make_review = False

    context={
        'product':product,
        'p_images':p_images,
        # 'address':address,
        'products':products, 
        'all_products':all_products,
        'reviews':reviews,   
        'review_form':review_form,
        'make_review':make_review,
    }
    return render (request,'core/product-details.html',context)


def tag_list(request,tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by('-id')

    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        'products':products,
        'tag':tag,
    }

    return render(request,'core/tags.html',context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user':user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }

    average_review = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse({
        'bool':True, 
        'context':context,
        'average_review':average_review, 
 
        })


# def search_view(request):
#     query = request.GET.get("q", "")
#     if query:
#         # Split the query into individual words
#         words = query.split()
#         # Create Q objects for each word
#         q_objects = Q()
#         for word in words:
#             q_objects |= Q(title__icontains=word)
#         # Filter products based on the combined Q objects
#         products = Product.objects.filter(q_objects).order_by('-date')
#     else:
#         products = Product.objects.none()  # Return an empty queryset if no query

#     context = {
#         'products': products,
#         'query': query,
#     }
#     return render(request, 'core/search.html', context)


def search_view(request):
    query = request.GET.get("q", "")
    if query:
        # Fetch all products and apply fuzzy search
        products = Product.objects.all().order_by('-date')
        filtered_products = [product for product in products if find_near_matches(query, product.title, max_l_dist=2)]
        
        # Check if there are any results
        products_found = bool(filtered_products)
        
        # If no products match the query, show all products
        if not products_found:
            filtered_products = []
    else:
        # If no query, show all products
        filtered_products = Product.objects.all().order_by('-date')
        products_found = True  # Set to True to indicate products are available
    
    context = {
        'products': filtered_products,
        'query': query,
        'products_found': products_found,
    }
    return render(request, 'core/search.html', context)

def filter_product(request):
    categories = request.GET.getlist("category[]")
    vendors = request.GET.getlist("vendor[]")

    min_price = request.GET["min_price"]
    max_price = request.GET["max_price"]

    products = Product.objects.filter(product_status="published").order_by('-id').distinct()

    products = products.filter(price__gte = min_price )
    products = products.filter(price__lte = max_price )

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()

    # if min_price:
    #     products = products.filter(price__gte=min_price)

    # if max_price:
    #     products = products.filter(price__lte=max_price)

    data = render_to_string("core/async/product-list.html",{"products":products})
    return JsonResponse({"data":data}) 


def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title':request.GET['title'],
        'qty':request.GET['qty'],
        'price':request.GET['price'],
        'id':request.GET['id'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty']=int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data=request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product
    
    return JsonResponse({"data":request.session['cart_data_obj'],'totalcartitem':len(request.session['cart_data_obj']) })