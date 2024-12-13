from django.shortcuts import render
from apps.product.models import Product, Shop

def index(request, pk):
    shop = Shop.objects.get(id=pk)
    products = Product.objects.filter(shop=shop)
    context = {
        'products': products,
        'shop': shop
    }
    return render(request, 'client/index.html', context)


def scanner(request):
    return render(request, 'client/scanner.html')


def pricing(request):
    return render(request, 'client/pricing.html')

def about(request):
    return render(request, 'client/about.html')

def contacts(request):
    return render(request, 'client/contacts.html')

def faq(request):
    return render(request, 'client/faq.html')

def features(request):
    return render(request, 'client/features.html')

def clients(request):
    return render(request, 'client/clients.html')