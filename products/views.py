from django.shortcuts import render
from .models import Product


def all_tickets(request):
    products = Product.objects.all()
    return render(request, 'all_tickets.html', {"products": products})


def buy_tickets(request):
    products = Product.objects.all()
    return render(request, 'buy_tickets.html', {"products": products})


def bug(request):
    products = Product.objects.all()
    return render(request, 'bug.html', {"products": products})


def feature(request):
    products = Product.objects.all()
    return render(request, 'feature.html', {"products": products})


def full_detail(request):
    products = Product.objects.all()
    return render(request, 'full_detail.html', {"products": products})
