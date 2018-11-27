# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def list_product(request):
    products = Product.objects.all()
    return render(request, 'simple_CRUD/products.html', {'products' : products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_product')
    return render(request, 'simple_CRUD/product-form.html', {'form' : form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_product')
    return render(request, 'simple_CRUD/product-form.html', {'form': form, 'product' : product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method =='POST':
        product.delete()
        return redirect('list_product')
    return render(request, 'simple_CRUD/product-delete-confirm.html', {'product' : product})