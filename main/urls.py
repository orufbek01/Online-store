from django.urls import path
from .models import *
from .views import *


urlpatterns = [
    # ---------------- Start Get url --------------- #

    # ------ Start Office url ----- #


    path('get_office', get_office),


    # ------ End Office url ----- #

    # ------ Start Color url ----- #


    path('get_color', get_color),


    # ------ End Color url ----- #

    # ------ Start Brand url ------ #


    path('get_brand', get_brand),


    # ------ End Brand url ------ #

    # ------ Start Category url ------ #


    path('get_category', get_category),


    # ------ End Category url ------ #

    # ------ Start Sub_category url ------ #


    path('get_sub_category', get_sub_category),


    # ------ End sub_category url ------ #

    # ------ Start Product url ------ #


    path('get_product', filter_product_by_price),


    # ------ End Product url ------ #

    # --------------- End Get url --------------- #


    # -------------- Start Filter url --------------- #

    # ------ Start filter-product-by-price url ------ #


    path('filter-product-by-price/<int:pk>/', filter_product_by_price),


    # ------ End filter-product-by-price url ------ #


    # ------ Start filter-product-by-category url ------ #


    path('filter_sub_category_by_category/<int:pk>/', filter_sub_category_by_category),


    # ------ End filter-product-by-category url ------ #


    # ------ Start filter-product-sub_category url ------ #


    path('filter_product_by_sub_subcategory/<int:pk>/', filter_product_by_sub_subcategory),


    # ------ End filter-product-by-sub_category url ------ #


    # ------ Start filter_product_by_brand url ------ #


    path('filter_product_by_brand/<int:pk>/', filter_product_by_brand),


    # ------ End filter_product_by_brand url ------ #
]