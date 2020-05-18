from django.contrib import admin

from .models import Brand,Categorys,ProductCategorys,Products,HomePage
# Register your models here.

#商标后台管理模型
class BrandAdmin(admin.ModelAdmin):
    fields = ('brandname', 'brandicon','brandurl') #表示可修改表中这些属性
    list_display = ('brandname', 'brandicon','brandurl') #展示表中哪些列
    search_fields = ('brandname', 'brandicon', 'brandurl') # 添加搜索字段
    list_per_page = 30 #设置每页显示多少条记录，默认是100条
    # ordering = ['-id'] #设置默认的排序字段 按照id倒序
    # list_editable 设置默认可编辑字段
    #list_editable = ['brandname', 'brandicon','brandurl']
    # 设置哪些字段可以点击进入编辑界面
    #list_display_links = ('brandname', 'brandicon')

#类别（大类）后台管理模型
class CategorysAdmin(admin.ModelAdmin):
    fields = ('name', 'showtype', 'imgUrl', 'desc')
    list_display = ('name', 'showtype', 'imgUrl', 'desc')
    search_fields = ('name', 'showtype', 'imgUrl', 'desc')
    list_per_page = 30
    list_display_links = ('name', 'showtype')

#产品类别（子类别）后台管理模型
class ProductCategorysAdmin(admin.ModelAdmin):
    fields = ('belongtocate', 'name', 'list_icon', 'thumbnail_img', 'blend_avatar', 'blend_desc')
    list_display = ('belongtocate', 'name', 'list_icon', 'thumbnail_img', 'blend_avatar', 'blend_desc')
    search_fields = ('name', 'blend_desc', 'belongtocate')
    list_per_page = 30
    # inlines = [Categorys]

#产品后台管理模型
class ProductsAdmin(admin.ModelAdmin):
    fields = ('belongtocategory', 'product_img', 'product_desc1', 'product_desc2')
    list_display = ('belongtocategory', 'product_img', 'product_desc1', 'product_desc2')
    search_fields = ('belongtocategory', 'product_img', 'product_desc1', 'product_desc2')
    list_per_page = 30

#主页面大图（一张图）管理模型
class HomePageAdmin(admin.ModelAdmin):
    fields = ('title', 'page_imgUrl','page_desc')
    list_display = ('title', 'page_imgUrl','page_desc')
    search_fields = ('title',)
    list_per_page = 30





admin.site.register(Brand, BrandAdmin)

admin.site.register(Categorys, CategorysAdmin)
admin.site.register(ProductCategorys, ProductCategorysAdmin)
admin.site.register(Products, ProductsAdmin)

admin.site.register(HomePage,HomePageAdmin)


