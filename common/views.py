from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_admin_index(request):
    return render(request,'common_templates/admin_index.html')

def common_customer_index(request):
    return render(request,'common_templates/customer_index.html')

def common_seller_index(request):
    return render(request,'common_templates/seller.html')    