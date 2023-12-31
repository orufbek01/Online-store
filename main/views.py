from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


# ---------- Start Get ---------- #

""" Start office view """


@api_view(['GET'])
def get_office(request):
    office = Office.objects.all()
    ser = OficeSerializer(office, many=True)
    return Response(ser.data)


""" End office view """

""" Start get color view """


@api_view(['GET'])
def get_color(request):
    color = Color.objects.all()
    ser = ColorSerializer(color, many=True)
    return Response(ser.data)


""" End color view """

""" Start brand view """


@api_view(['GET'])
def get_brand(request):
    brand = Brand.objects.all()
    ser = BrandSerializer(brand, many=True)
    return Response(ser.data)


""" End brend view """

""" Start category view """


@api_view(['GET'])
def get_category(request):
    category = Category.objects.all()
    ser = CategorySerializer(category, many=True)
    return Response(ser.data)


""" End category view """

""" Start sub_category view """


@api_view(['GET'])
def get_sub_category(request):
    category = Sub_category.objects.all()
    ser = Sub_CategorySerializer(category, many=True)
    return Response(ser.data)


""" End sub_category view """

""" Start Product view """
@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    ser = ProductSerializers(Product, many=True)
    return Response(ser.data)


""" End Product view """


# ---------- End Get ---------- #

# ----------Start Filter ---------- #


""" Start Filter Product by price  """


@api_view(['GET'])
def filter_product_by_price(request):
    start_price = request.objects.GET.get('s_price')
    end_price = request.objects.GET.get('e_price')
    products = Product.objcts.filter(price__get=start_price, price__lte=end_price)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)


""" End Filter Product by price  """

""" Start Filter Sub_Category by Category """


@api_view(['GET'])
def filter_sub_category_by_category(request,pk):
    category = Category.objects.get(pk=pk)
    filter = Sub_category.objects.filter(category=category)
    ser = Sub_CategorySerializer(filter, many=True)
    return  Response(ser.data)


""" End Filter Sub_Category by Category """

""" Start Filter Product by Sub_Category """


@api_view(['GET'])
def filter_product_by_sub_subcategory(request,pk):
    sub_category = Sub_category.objects.get(pk=pk)
    product = Product.objects.filter(sub_category=sub_category)
    ser = ProductSerializers(product, many=True)
    return Response(ser.data)

""" End Filter Product by Sub_Category """

""" Start Filter Product by Brand"""


@api_view(['GET'])
def filter_product_by_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    product = Product.objects.filter(brand=brand)
    ser = ProductSerializers(product,many=True)
    return Response(ser.data)


""" End Filter Product by Brand"""

""" Start Filter Product rating """








