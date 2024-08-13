from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

STATUS_CHOICE = (
    ("process","Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
    ("cancel", "Cancel"),
)

STATUS= (
    ("draft","Draft"),
    ("disabled", "Didsabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("rejected","Rejected"),
    ("published", "Published"),
)
RARING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Category(models.Model):
    cid = ShortUUIDField(unique=True,length = 10,max_length = 20,prefix ="cat", alphabet="abcdefg1234" )
    title = models.CharField(max_length=100,default="Food")
    image = models.ImageField(upload_to="category", default="category/default.png")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
       return self.title 

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix ="ven", alphabet="abcdefg1234")

    title = models.CharField(max_length=100,default="Netlify")
    image = models.ImageField(upload_to=user_directory_path,default="vendor.png")
    cover_image = models.ImageField(upload_to=user_directory_path,default="vendor.png")
    # description = models.TextField(null=True, blank=True,default="This is a default description")
    description = RichTextField(null=True, blank=True,default="This is a default description")
    # address = models.TextField(max_length=100 , default="123 Main Street")
    address = RichTextField(max_length=100 , default="123 Main Street")

    contact = models.CharField(max_length=100, default="000000000000")
    chat_resp_time = models.CharField(max_length=100, default="00:00:00")
    shipping_on_time = models.CharField(max_length=100, default="00:00:00")
    authenticate_rating = models.CharField(max_length=100, default="0")
    days_return = models.CharField(max_length=100, default="0")
    warranty_period = models.CharField(max_length=100, default="0")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
       return self.title


class Tags(models.Model):
    pass

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix ="pr", alphabet="abcdefg1234")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,related_name="Category") 
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True,related_name="vendor") 

    title = models.CharField(max_length=100,default="Frsh Pear")
    image = models.ImageField(upload_to=user_directory_path,default="product/default.png")
    # description = models.TextField(null=True, blank=True,default="This is a default description")
    description = RichTextField(null=True, blank=True,default="This is a default description")

    price = models.IntegerField(max_length = 99999,default=199)
    old_price = models.IntegerField(max_length = 99999,default=299)

    # specifiction = models.TextField(null=True, blank=True, )
    specifiction = RichTextField(null=True, blank=True, )
    type_of_food = models.CharField(max_length=100,default="Organic")
    stock_count = models.IntegerField(max_length=100000,blank=True,default=100)
    life = models.IntegerField(max_length=800,blank=True,default=70)

    tags = TaggableManager(blank=True)

    product_status = models.CharField(max_length=10, choices=STATUS, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digitial = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix ="sku", alphabet="abcdefg1234")

    date = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
       return self.title

    def get_percentage(self):
        percentage = (self.price/self.old_price) * 100
        return round(percentage)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name="p_images",on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="product-images",default="product.jpg")
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Products Images"



############################----------------Cart,   Order,   OrderItems,---------------------##############################################

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length = 99999,default=199)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(max_length=30, choices=STATUS_CHOICE, default="processing")


    class Meta:
        verbose_name_plural = "Card Order"



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, null=True)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200 )
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(max_length = 99999,default=199)
    total = models.IntegerField(max_length = 99999,default=199)

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))



############################------ Product Revie,Wishlist,Address --------################################################################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,related_name="reviews")
    # review = models.TextField(max_length=500, null=True, blank=True)
    review = RichTextField(max_length=500, null=True, blank=True)
    rating = models.IntegerField(choices=RARING, default=1)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def get_rating(self):
       return self.rating



class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Wish List"

    def __str__(self):
       return self.product.title

    def get_rating(self):
        return self.rating


class Address(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"



    


