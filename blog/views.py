from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
def blog(request):

    return render(request,'blog.html')


def all_countries(request):
    products = Product.objects.all()
    context = {
        'products': products

    }
    return render(request, 'next_to_page.html',context)




def product_detail(request, id):
    products = get_object_or_404(Product, id=id)
    context = {
        'products': products
    }
    return render(request, 'detail.html', context)


