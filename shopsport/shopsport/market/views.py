from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
from .models import Brand,HomePage,Products,ProductCategorys,Categorys
import json
from django.core import serializers

def responseUtil(json_list):
    #解决中文乱码问题 ensure_ascii=False charset=utf-8
    json_data = json.dumps(json_list, ensure_ascii=False)
    response = HttpResponse()
    response['Content-Type'] = "application/json; charset=utf-8"
    response["Access-Control-Allow-Origin"] = "*"
    response.write(json_data)
    return response

#左上角品牌接口
def brand(request):
    try:
        brands = Brand.objects.all()
        json_list = []

        for brand in brands:
            brand_dict = {}
            brand_dict['brandname'] = brand.brandname
            brand_dict['brandicon'] = str(brand.brandicon)
            brand_dict['brandurl'] = brand.brandurl
            json_list.append(brand_dict)

        response = responseUtil(json_list)
        return response
    except:
        json_list = []
        response = responseUtil(json_list)
        return response


#主页大图接口
def homePage(request):
    try:
        home_pages = HomePage.objects.all().order_by('-id')[:1]
        for home_page in home_pages:
            home_title = home_page.title
            page_imgUrl = str(home_page.page_imgUrl)
            page_desc = home_page.page_desc

        json_data = {
            "home_title": home_title,
            "home_imgUrl": page_imgUrl,
            "home_desc": page_desc
        }
        response = responseUtil(json_data)
        return response
    except:
        json_data = []
        response = responseUtil(json_data)
        return response

#主页大图对应上面（主）分类  img一定要加str不然不会序列化
def homeCategory(request):
    json_list = []
    try:
        categorys = Categorys.objects.all()
        for category in categorys:
            json_list.append(
                {
                    "category_name":category.name,                   
                    "category_imgUrl":str(category.imgUrl),
                    "category_desc":category.desc
                }
            )
        json_list = json_list[:3]
        response = responseUtil(json_list)
        return response
    except:
        json_list = []
        response = responseUtil(json_list)
        return response


#通过类或子类参数及起点与步长返回产品信息
def productsByCategory(request):
    categoryName = request.GET.get("categoryName").upper()
    #get参数都是str类型的 需要转化为int
    #起点
    start = int(request.GET.get("start"))
    #步长
    limit = int(request.GET.get("limit"))
    json_list = []
    try:
        subCateList = []
        for category in Categorys.objects.all():
            for subCate in category.productcategorys_set.all():
                subCateList.append(subCate.name)

       #通过子类查询
        if categoryName.title() in subCateList:

            productCategory = ProductCategorys.objects.get(name = categoryName.title())
            products = productCategory.products_set.all()[start:start + limit]
            for product in products:
                json_list.append(
                    {
                        "product_img": str(product.product_img),
                        "product_desc1": product.product_desc1,
                        "product_desc2": product.product_desc2
                    }
                )

            response = responseUtil(json_list)
            return response
        #通过父类查询
        elif categoryName in [category.name for category in Categorys.objects.all()]:
            category = Categorys.objects.get(name = categoryName)
            for subCategory in category.productcategorys_set.all():
                for product in subCategory.products_set.all():
                    json_list.append(
                        {
                            "product_img": str(product.product_img),
                            "product_desc1": product.product_desc1,
                            "product_desc2": product.product_desc2
                        }
                    )

            json_list = json_list[start:start + limit]
            response = responseUtil(json_list)
            return response
        else:
            json_list = []
            response = responseUtil(json_list)
            return response
    except:
        json_list = []
        response = responseUtil(json_list)
        return response
		
#返回所有子类信息
def subCategorys(request):
    json_list = []
    try:
        categorys = Categorys.objects.all()
        showType = "L"
        for category in categorys:
            cate_dict = {}
            cate_dict['categoryName'] = category.name
            cate_dict['showType'] = category.showtype
            cate_dict['subCategory'] = []
            print(cate_dict)

            if category.showtype == "T":
                showType = "T"
            elif category.showtype == "B":
                showType = "B"
            else:
                showType = "L"
            for subCategory in category.productcategorys_set.all():
                if showType == "L":
                    cate_dict['subCategory'].append(
                        {
                            "subCateName": subCategory.name,
                            "list_icon": str(subCategory.list_icon)
                        }
                    )
                elif showType == "T":
                    cate_dict['subCategory'].append(
                        {
                            "subCateName": subCategory.name,
                            "thumbnail_img": str(subCategory.thumbnail_img)
                        }
                    )
                elif showType == "B":
                    cate_dict['subCategory'].append(
                        {
                            "subCateName": subCategory.name,
                            "blend_avatar": str(subCategory.blend_avatar),
                            "blend_desc": subCategory.blend_desc
                        }
                    )
            json_list.append(cate_dict)
        response = responseUtil(json_list)
        return response

    except:
        json_list = []
        response = responseUtil(json_list)
        return response













