from orderlist.order.models import customer, product
from django.shortcuts import render
from order.models import *
from django.contrib import messages
# Create your views here.

def insert_data_customer(request):
    # first_name = "Dishan"
    # last_name = "Bhardwaj"
    # contact_no = 82938034399
    # pincode = 12345
    try:
        record = customer.objects.bulk_create([customer(first_name = "Dishan",last_name = "Bhardwaj",contact_no = 8200906559,pincode = 12345),
                customer(first_name = "Karan",last_name = "Shah",contact_no = 9014550066,pincode = 45896),
                customer(first_name = "Dhruv",last_name = "Pandya",contact_no = 2589659833,pincode = 45894))]

        messages.info(request,'Data has been inserted successfully')

        return render(request,'mainpage.html', {})

    except:

        messages.info(request,'There has been an issue while creating data')

        return render(request,'mainpage.html', {})

def insert_data_product(request):
    try:
        record = customer.objects.bulk_create([product(name = "Gold",unit_price = 1000.00),
                product(name = "Bronze",unit_price = 800.00),
                product(name = "Silver",unit_price = 900.80)),
                product(name = "Copper",unit_price = 700.00))]

        messages.info(request,'Data has been inserted successfully')

        

    except:

        messages.info(request,'There has been an issue while creating data')

        return render(request,'mainpage.html', {})

def open_mainpage(request,context={}):

    data = customer.objects.all()
    data2 = product.objects.all()

    context["customer"] = data
    context["product"] = data2

    return render(request,'mainpage.html',context)

def insert_data_order(request):
    customer = request.POST.get("customer")
    product = request.POST.get("product")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    total = request.POST.get("total")

    record = order(customer_id = customer,product_id = product,unit_price = price,qty = quantity,total_price = total)
    record.save()

    messages.info(request,'Data was inserted successfully')

    return render(request,'mainpage.html', {})

def edit_order(request):

    customer = request.POST.get("customer")
    product = request.POST.get("product")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    total = request.POST.get("total")


    order = order.objects.get(customer_id = customer)

    order.product_id = product
    order.unit_price = price
    order.qty = quantity
    order.total_price = total

    order.save()

    messages.info(request,'Data was edited successfully')

    return render(request,'mainpage.html', {})