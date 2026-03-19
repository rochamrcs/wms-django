from django.shortcuts import redirect, render
from products.models import Product
from products.forms import ProductForm

def products(request):
    search = request.GET.get('q')
    products_list = Product.objects.all()

    if search:
        products_list = Product.objects.filter(name__icontains=search)

    return render(request, 'products.html', {"products_list": products_list})

def new_product(request):
    if request.method == 'POST':
        new_product_form = ProductForm(request.POST)
        print(new_product_form)

        if new_product_form.is_valid():
            new_product_form.save()
            return redirect('products:products')
    else:
        new_product_form = ProductForm()
    return render(request, 'new_product.html', {'new_product': new_product_form})