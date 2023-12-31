from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from main.serializers import *


""" Start Address CRUD """


@api_view(['POST'])
def create_address(request):
    name = request.POST['name']
    address = Address.objects.create(name=name)
    ser = AddressSerializers(address)
    return Response(ser.data)


@api_view(['PUT'])
def edit_address(request, pk):
    address = Address.objects.get(pk=pk)
    name = request.data.get('name')
    if name is not None:
        address.name = name
    address.save()
    ser = AddressSerializer(address)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_address(request, pk):
    address = Address.objects.get(pk=pk)
    address.delete()
    return Response({'message': "Address obyekti o'chirildi"})


""" End Address CRUD """

""" Start Category CRUD """


@api_view(['POST'])
def create_category(request):
    name = request.POST['name']
    category = Category.objects.create(name=name)
    ser = CategorySerializer(category)
    return Response(ser.data)


@api_view(['PUT'])
def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    name = request.data.get('name')
    if name is not None:
        category.name = name
    category.save()
    ser = CategorySerializer(category)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return Response({'message': "Category obyekti o'chirildi"})


""" End Category CRUD """

""" Start Sub_category CRUD  """


@api_view(['POST'])
def create_sub_category(request):
    name = request.POST['name']
    category = request.POST['category']
    sub_category = Sub_category.objects.create(
        name=name,
        category=category
    )
    ser = Sub_categorySerializer(sub_category)
    return Response(ser.data)


@api_view(['PUT'])
def edit_sub_category(request, pk):
    sub_category = Sub_category.objects.get(pk=pk)
    name = request.data.get('name')
    category = request.data.get['category']
    if name is not None:
        sub_category.name = name
    if category is not None:
        sub_category.category = category
    sub_category.save()
    ser = Sub_categorySerializer(sub_category)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_sub_category(request, pk):
    sub_category = Sub_category.objects.get(pk=pk)
    sub_category.delete()
    return Response({'message': "Sub category obyekti o'chirildi"})


""" End Sub_category CRUD """

""" Start Brand CRUD """


@api_view(['POST'])
def create_brand(request):
    name = request.POST['name']
    brand = Brand.objects.create(name=name)
    ser = BrandSerializer(brand)
    return Response(ser.data)


@api_view(['PUT'])
def edit_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    name = request.data.get('name')
    if name is not None:
        brand.name = name
    brand.save()
    ser = BrandSerializer(brand)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.delete()
    return Response({'message': "Brand obyekti o'chirildi"})


""" End Brand CRUD """

"""Start Color CRUD """


@api_view(['POST'])
def create_color(request):
    name = request.POST['name']
    img = request.FILES['img']
    color = Color.objects.create(
        name=name,
        img=img
    )
    ser = ColorSerializer(color)
    return Response(ser.data)


@api_view(['PUT'])
def edit_color(request, pk):
    color = Color.objects.get(pk=pk)
    name = request.data.get('name')
    img = request.data.get('img')
    if name is not None:
        color.name = name
    if img is not None:
        color.img = img
    color.save()
    ser = ColorSerializer(color)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_color(request, pk):
    color = Color.objects.get(pk=pk)
    color.delete()
    return Response({'message': "Color obyekti o'chirildi"})


""" End Color CRUD """

""" Start Image CRUD """

@api_view(['POST'])
def create_image(request):
    img = request.FILES['img']
    image = Image.objects.create(
        img=img
    )
    ser = ImageSerializer(img)
    return Response(ser.data)


@api_view(['PUT'])
def edit_image(request, pk):
    image = Image.objects.get(pk=pk)
    img = request.data.get('img')
    if img is not None:
        image.img = img
    image.save()
    ser = ImageSerializer(image)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_image(request, pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    return Response({'message': "Image obyekti o'chirildi"})


""" End Image CRUD """

""" Start Size_category CRUD """


@api_view(['POST'])
def create_size_category(request):
    name = request.POST['name']
    size_category = Size_category.objects.create(name=name)
    ser = Size_categorySerializer(size_category)
    return Response(ser.data)


@api_view(['PUT'])
def edit_size_category(request, pk):
    size_category = Size_category.objects.get(pk=pk)
    name = request.data.get('name')
    if name is not None:
        size_category.name = name
    size_category.save()
    ser = BrandSerializer(size_category)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_size_category(request, pk):
    size_category = Size_category.objects.get(pk=pk)
    size_category.delete()
    return Response({'message': "Size_category obyekti o'chirildi"})


""" End Size_category CRUD """

""" Start Card CRUD """


@api_view(['POST'])
def create_card(request):
    user = request.user
    product = request.POST['product']
    total_price = request.POST['total_price']
    quantity = request.POST['quantity']
    card = Card.objects.create(
        user=user,
        product=product,
        total_price=total_price,
        quantity=quantity,
    )
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['PUT'])
def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    user = request.user
    product = request.data.get('product')
    total_price = request.data.get('total_price')
    quantity = request.data.get('quantity')
    if user is not None:
        card.user = user
    if product is not None:
        card.product = product
    if total_price is not None:
        card.total_price = total_price
    if quantity is not None:
        card.quantity = quantity
    card.save()
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_card(request, pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return Response({'message': "Card obyekti o'chirildi"})


""" End Card CRUD """

""" Start Saved CRUD """


@api_view(['POST'])
def create_saved(request):
    user = request.user
    product = request.POST['name']
    saved = Saved.objects.create(
        user=user,
        product=product,
    )
    ser = SavedSerializer(saved)
    return Response(ser.data)


@api_view(['PUT'])
def edit_saved(request, pk):
    saved = Saved.objects.get(pk=pk)
    user = request.user
    product = request.data.get('product')
    if user is not None:
        saved.user = user
    if product is not None:
        saved.product = product
    saved.save()
    ser = SavedSerializer(saved)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_saved(request, pk):
    saved = Saved.objects.get(pk=pk)
    saved.delete()
    return Response({'message': "Saved obyekti o'chirildi"})



""" End Saved CRUD """

""" Start Office CRUD """


@api_view(['POST'])
def create_office(request):
    name = request.POST['name']
    number = request.POST['number']
    address = request.POST['address']
    office = Office.objects.create(
        name=name,
        number=number,
        address=address,
    )
    ser = OfficeSerializer(office)
    return Response(ser.data)

@api_view(['PUT'])
def edit_office(request, pk):
    office = Office.objects.get(pk=pk)
    name = request.data.get('name')
    number = request.data.get('number')
    address = request.data.get('address')
    if name is not None:
        office.name = name
    if number is not None:
        office.number = number
    if address is not None:
        office.address = address
    office.save()
    ser = OfficeSerializer(office)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_office(request, pk):
    office = Office.objects.get(pk=pk)
    office.delete()
    return Response({'message': "Office obyekti o'chirildi"})


""" End Office CRUD """

""" Start Order CRUD """


@api_view(['POST'])
def create_order(request):
    user = request.user
    card = request.POST.getlist('card')
    pass_number = request.POST['pass_number']
    is_delivery = request.POST['is_delivery']
    extra_phone_number = request.POST['extra_phone_number']
    payment_type = request.POST['payment_type']
    office = request.POST['office']
    lat = request.POST['lat']
    lot = request.POST['lot']
    order = Order.objects.create(
        user_id=user,
        card=card,
        pass_number=pass_number,
        is_delivery=is_delivery,
        extra_phone_number=extra_phone_number,
        payment_type=payment_type,
        office_id=office,
        lat=lat,
        lot=lot,
    )
    for i in card:
        order.card.append(i)
        order.save()
    ser = OrderSerializer(order)
    return Response(ser.data)


@api_view(['PUT'])
def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    user = request.user
    card = request.data.get('card')
    pass_number = request.data.get('pass_number')
    is_delivery = request.data.get('is_delivery')
    extra_phone_number = request.data.get('extra_phone_number')
    payment_type = request.data.get('payment_type')
    office = request.data.get('office')
    lat = request.data.get('lat')
    lot = request.data.get('lot')
    if user is not None:
        order.user = user
    if card is not None:
        order.card = card
    if pass_number is not None:
        order.pass_number = pass_number
    if is_delivery is not None:
        order.is_delivery = is_delivery
    if extra_phone_number is not None:
        order.extra_phone_number = extra_phone_number
    if payment_type is not None:
        order.payment_type = payment_type
    if office is not None:
        order.office = office
    if lat is not None:
        order.lat = lat
    if lot is not None:
        order.lot = lot
    order.save()
    ser = OrderSerializer(order)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response({'message': "Order obyekti o'chirildi"})


""" End Order CRUD """

