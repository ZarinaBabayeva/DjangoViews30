from django.shortcuts import render
from app.models import * 
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
# Create your views here.

def product_list_view(request):
    context = {
        "products":Product.objects.annotate(total_price = Coalesce(F('price') - F ('discount_price'),0,output_field = FloatField())),
    }

    return render(request , 'products/list.html', context)

def product_detail_view(request, id):
    context = {
        "id": id,
        "products":Product.objects.annotate(total_price = Coalesce(F('price') - F ('discount_price'),0,output_field = FloatField())),
    }
    return render(request , 'products/product_detail.html', context)