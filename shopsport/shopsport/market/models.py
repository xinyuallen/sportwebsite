from django.db import models
from django.contrib import admin

# Create your models here.
#品牌表(品牌名，品牌图标，品牌链接)
class Brand(models.Model):
    brandname = models.CharField(max_length=20, null=False, unique=True)
    brandicon = models.ImageField(upload_to="brandicon")
    brandurl = models.URLField()

    def __str__(self):
        return self.brandname

# 类别表（类别名，显示方式,类别的图片，类别的描述信息）
class Categorys(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    SHOWTYPE_CHOICE = (("L", "List"), ("T", "Thumbnail"), ("B", "Blend"))
    showtype = models.CharField(max_length=10, choices= SHOWTYPE_CHOICE, null=False, blank=False)
    imgUrl = models.ImageField(upload_to="categorysimg")
    desc = models.TextField(null=False, blank=False, default="this is category's description")

    def __str__(self):
        return self.name

#小类表（具体产品类别表 ）
class ProductCategorys(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    list_icon = models.ImageField(upload_to="list_icon", null=True, blank=True)
    thumbnail_img = models.ImageField(upload_to="thumbnail_img", null=True, blank=True)
    blend_avatar = models.ImageField(upload_to="blend_avatar", null=True, blank=True)
    blend_desc = models.TextField(null=True, blank=True)
    belongtocate = models.ForeignKey('Categorys',to_field='name', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def show_by_showtype(self):
        if self.belongtocate.showtype == "List":
            fields = ('belongtocate', 'name', 'list_icon')
            list_display = ('belongtocate', 'name', 'list_icon')

# 产品表(产品图片，产品描述信息1【必填】，产品描述信息2【选填】)
class Products(models.Model):
    product_img = models.ImageField(upload_to="products_img")
    product_desc1 = models.TextField(null=True, blank=True)
    product_desc2 = models.TextField(null=True, blank=True)
    belongtocategory = models.ForeignKey('ProductCategorys',to_field='name', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_img)

#首页的展示大图
class HomePage(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    page_imgUrl = models.ImageField(upload_to="page_img")
    page_desc = models.TextField(null=False, blank=False, default="this is homepage's picture description")

    def __str__(self):
        return self.title





