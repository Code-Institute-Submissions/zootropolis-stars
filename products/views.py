from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ A view to show all the products and
    sorting queries
    """
    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

    context = {
        "products": products,
        "current_categories": categories,
    }
    return render(request, 'products/products.html', context)


def product_detail_view(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }
    return render(request, 'products/product_detail.html', context)
