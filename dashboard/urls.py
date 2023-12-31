from django.urls import path
from .views import *

urlpatterns = [
    # ------ Start Address CRUD ------ #


    path('create-address/', create_address),
    path('edit-address/<int:pk>/', edit_address),
    path('delete-address/<int:pk>/', delete_address),


    # ------ End Address CRUD ------ #

    # ------ Start Category CRUD ------ #


    path('create-category/', create_category),
    path('edit-category/<int:pk>/', edit_category),
    path('delete-address/<int:pk>/', delete_category),


    # ------ End Category CRUD ------ #


    # ------ Start Sub_Category CRUD ------ #


    path('create-sub_category/', create_sub_category),
    path('edit-sub_category/<int:pk>/', create_address),
    path('delete-sub_category/<int:pk>/', delete_sub_category),


    # ------ End Sub_Category CRUD ------- #


    # ------ Start Order CRUD ------ #


    path('create-order/', create_order),
    path('edir-order/<int:pk>/', edit_order),
    path('delete-order/<int:pk>/', delete_order),


    # ------ End Order CRUD ------ #


    # ----- Start Brand CRUD ------ #


    path('create-brand/', create_brand),
    path('edit-brand/<int:pk>/', edit_brand),
    path('delete-brand/<int:pk>/', delete_order),

    # ------ End Brand CRUD ------ #


    # ------ Start Card CRUD ----- #


    path('create-card/', create_card),
    path('edit-card/<int:pk>/', edit_card),
    path('delete-card/<int:pk>/', delete_card),

    # ------ End Card CRUD ------ #


    # ------ Start Color CRUD ------ #


    path('create-color/', create_color),
    path('edit-color/<int:pk>/', edit_color),
    path('delete-color/<int:pk>/', delete_color),


    # ------- End Color CRUD ------ #


    # ------ Start Office CRUD ------ #


    path('create-office/', create_office),
    path('edit-office/<int:pk>/', edit_office),
    path('delete-office/<int:pk>/', delete_office),


    # ------ End Office CRUD ----- #


    # ------ Start Saved CRUD ------ #

    path('create-saved/', create_saved),
    path('edit-saved/<int:pk>/', edit_saved),
    path('delete-saved/<int:pk>/', delete_saved),

    # ------ End Saved CRUD ------ #


    # ----- Start Size_Category ------ #


    path('create-size_category/', create_size_category),
    path('edit-size_category/<int:pk>/', edit_size_category),
    path('delete-size_category/<int:pk>/', delete_size_category),

    # ------ End Size_Category ------ #


    # ------ Start Image CRUD ------ #


    path('create-image/', create_image),
    path('edit-image/<int:pk>/', edit_image),
    path('delete-image/<int:pk>/', delete_image),

    # ------ End Image CRUD ------ #
]