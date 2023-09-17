from django.shortcuts import render ,redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import Products
from django.views import View
from .forms import AddProductForm

def all_products(request:HttpRequest)->HttpResponse:
    """Функция для просмотра всех товаров"""
    products: Products = Products.objects.all()
    return render(
        request=request,
        template_name='main/all_products.html',
        context={
            'products':products
        }
    )

class AddProduct(View):
    """Класс для добавления нового продукта"""
    template_name = 'main/add_product.html'
    def get(self,request:HttpRequest)->HttpResponse:
        form = AddProductForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form':form
            }
        )

    def post(self,request:HttpRequest)->HttpResponse:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product : Products = Products(
                title = form.cleaned_data['title'],
                photo = form.cleaned_data['photo'],
                price = form.cleaned_data['price'],
                category = form.cleaned_data['category'],
                description = form.cleaned_data['description']
            )
            new_product.save()
            return redirect('success_page')
        else:
            return HttpResponse('<h1>Форма не валидна</h1>')

def success_page(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='main/success_page.html',
        context={}
    )

def fail_page(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='main/fail.html',
        context={}
    )

def product_page(request:HttpRequest,product_id:int)-> HttpResponse:
    try:
        product : Products = Products.objects.get(pk = product_id)
        if product:
            return render(
                request=request,
                template_name='main/product_page.html',
                context={
                    'product':product
                }
            )
    except Exception as exc:
        return HttpResponse(f'<h1>Ошибка: {exc}')

class DeleteProductView(View):
    """Класс для удаления продуктов"""
    template_name = 'main/delete_product.html'
    def get(self,request:HttpRequest)->HttpResponse:
        products: Products = Products.objects.all()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'products':products
            }
        )
    
def success_page_delete(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='main/success_page_delete.html',
        context={}
    )

def fail_page_delete(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='main/fail_page_delete.html',
        context={}
    )

def delete_product_by_id(request: HttpRequest, product_id: int) -> HttpResponse:
    if request.method == 'POST':
        try:
            product = Products.objects.get(pk=product_id)
            product.delete()
            return redirect('success_page_delete')
        except Products.DoesNotExist:
            return redirect('fail_page_delete')
    else:
        products = Products.objects.all()
        return render(
            request=request,
            template_name='main/delete_product.html',
            context={
                'products': products
            }
        )
