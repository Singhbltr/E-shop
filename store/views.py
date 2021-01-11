from django.shortcuts import render
from django.http import HttpResponse
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.
def index(request):
    products=None
    categories=Category.get_all_categories()
    categoryID=(request.GET.get('category'))
    #print(request.GET)
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
    else:
        products=Product.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    #return render(request,'orders/order.html')
    #print(products)

    return render(request,'index.html',data)
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        #validaton
        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        error_message=None
        if not first_name:
            error_message="First Name Required"
        elif len(first_name)<3:
            error_message="First Name Must Be Atleast 3 Char"
        elif not phone:
            error_message="Phone Number Required"
        elif len(phone)<10:
            error_message="Phone Number Must be size of 10"
        elif len(password)<6:
            error_message="Password must be atleast 6 char long"

        #saving
        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer=Customer(first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password)
            customer.register()
            return render(request,'signup.html')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)