from core.views import *
from django.db.models import Min,Max
# this for the importing the all objects from database to base html page

def default (request):
    categories = Category.objects.all()
    vendor = Vendor.objects.all()
    min_max_price = Product.objects.aggregate(Min("price"),Max("price"))
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None    
    return {
        'categories':categories,
        'vendor':vendor,
        'address':address,
        'min_max_price':min_max_price,
    }