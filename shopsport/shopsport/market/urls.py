from django.contrib import admin
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from market import views

urlpatterns = [
    path('brand/', views.brand, name="brand"),
    path('homePage/', views.homePage, name="homePage"),
    path('homeCategory/', views.homeCategory, name="homeCategory"),
    path("productsByCategory/", views.productsByCategory, name="productsByCategory"),
	path("subCategorys/", views.subCategorys, name="subCategorys"),



]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)