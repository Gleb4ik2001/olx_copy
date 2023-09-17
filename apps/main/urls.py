from django.urls import path
from .views import all_products, AddProduct, success_page, product_page, DeleteProductView, fail_page,fail_page_delete,success_page_delete,delete_product_by_id
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',all_products,name='all_products'),
    path('add_product/',AddProduct.as_view(),name='add_product'),
    path('success_page/',success_page,name='success_page'),
    path('product/<int:product_id>/',product_page,name='product_page'),
    path('delete_product/',DeleteProductView.as_view(),name='delete_product'),
    path('fail_page/',fail_page,name='fail_page'),
    path('fail_page_delete/',fail_page_delete,name='fail_page_delete'),
    path('success_page_delete/',success_page_delete,name='success_page_delete'),
    path('delete_product/<int:product_id>/',delete_product_by_id,name='delete_product_by_id')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)