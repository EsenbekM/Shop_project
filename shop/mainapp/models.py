from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from PIL import Image
from django.urls import reverse

User = get_user_model()

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model':ct_model, 'slug':obj.slug})

class MinResolutionErrorExeption(Exception):
    pass


class MaxResolutionErrorExeption(Exception):
    pass



class LatestProductsManager:

    @staticmethod
    def get_product_for_main_page(*args, **kwargs):
        whith_respect_to = kwargs.get('whith_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model_in=args)
        for ct_model in ct_models:
            model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_product)
        if whith_respect_to:
            ct_model = ContentType.objects.filter(model=whith_respect_to)
            if ct_model.exists():
                if whith_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__.meta.model_name.startswith(whith_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    
    objects = LatestProductsManager()



class Category(models.Model):
    ''' Create a Categories in the shop '''
    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    ''' Create a Product in the shop '''
    # MIN_RESOLUTION = (400,400)
    # MAX_IMAGE_SIZE = 3145728

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Product category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Product title')
    slug = SlugField(unique=True)
    image = ImageField(verbose_name='Product image')
    description = TextField(verbose_name='Product description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Product price')


    def __str__(self):
        return self.title


    # def save(self, *args, **kwargs):
    #     image = self.image
    #     img = Image.open(image)
    #     min_width, min_height = self.MIN_RESOLUTION
    #     max_width, max_height = self.MIN_RESOLUTION
    #     if img.height < min_height or img.width < min_width:
    #         raise MinResolutionErrorExeption('resolution of image less than the minimum!')
    #     if img.height > max_height or img.width > max_width:
    #         raise MaxResolutionErrorExeption('resolution of image bigger than the maximum!')
    #     super().save(*args, **kwargs)


class Laptop(Product):
    '''Class for Laptops'''

    diagonal = models.CharField(max_length=255, verbose_name="diagonal")
    matrix = models.CharField(max_length=255, verbose_name="display matrix")
    proccesor_freq = models.CharField(max_length=255, verbose_name="proccesor freq")
    ram = models.CharField(max_length=255, verbose_name="RAM")
    videp_card = models.CharField(max_length=255, verbose_name="videp card")
    time_without_charge = models.CharField(max_length=255, verbose_name="time without charge")
    
    def __str__(self):
        return (f"{self.category.name} : {self.title}")

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Smartphone(Product):
    '''Class for Laptops'''

    diagonal = models.CharField(max_length=255, verbose_name="diagonal")
    matrix = models.CharField(max_length=255, verbose_name="display matrix")
    accum = models.CharField(max_length=255, verbose_name="accum volume")
    ram = models.CharField(max_length=255, verbose_name="RAM")
    sd = models.CharField(max_length=255, verbose_name='SD volume')
    main_cam_mp = models.CharField(max_length=255, verbose_name='main camera')
    front_cam_mp = models.CharField(max_length=255, verbose_name='frontal camera')

    
    def __str__(self):
        return (f"{self.category.name} : {self.title}")

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):
    ''' Create a CartProduct in the shop '''
    user = models.ForeignKey("Customer", verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name='Cart', on_delete=models.CASCADE, related_name='related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')


    def __str__(self):
        return (f"Cart Product: {self.product.title}")


class Cart(models.Model):
    ''' Create a Cart in the shop '''
    owner = models.ForeignKey("Customer", verbose_name='owner', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveBigIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)



class Customer(models.Model):
    ''' Create a User in the shop '''
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='User address')

    
    def __str__(self):
        return (f"Customer: {self.user.first_name} {self.user.last_name}")