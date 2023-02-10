from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.core.models import BaseModel


class ProductBaseModel(BaseModel):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    class Meta:
        db_table = "category"


class ProductSize(ProductBaseModel):
    class Meta:
        db_table = "product_size"


class ProductColor(ProductBaseModel):
    class Meta:
        db_table = "product_color"


class ProductType(ProductBaseModel):
    class Meta:
        db_table = "product_type"


class Product(ProductBaseModel):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.CharField(max_length=200)
    sold = models.CharField(max_length=200)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    product_colors = models.ForeignKey(ProductColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"


class MTProductType(BaseModel):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "mt_product_type"


class Rating(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    star = models.IntegerField()

    class Meta:
        db_table = "rating"


class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.IntegerField()

    class Meta:
        db_table = "comment"


class File(BaseModel):
    photo_preview_url = models.CharField(max_length=200)
    photo_realistic_url = models.CharField(max_length=200)

    class Meta:
        db_table = "file"


class MTFile(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        db_table = "mt_file"


class BannerPhoto(BaseModel):
    url = models.CharField(max_length=200)
    type = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        db_table = "mt_file"
