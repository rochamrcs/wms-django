from django.shortcuts import redirect, render
from products.models import Product
from products.forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login_form')
def products(request):
    search = request.GET.get('q')
    filter_status = request.GET.get('status')

    products_list = Product.objects.all()

    if search:
        products_list = products_list.filter(
            Q(name__icontains=search) |
            Q(product_code__icontains=search)
        )

    if filter_status == "ativo":
        products_list = products_list.filter(status=True)

    elif filter_status == "inativo":
        products_list = products_list.filter(status=False)

    return render(request, 'products.html', {"products_list": products_list})


@login_required(login_url='accounts:login_form')
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