from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .forms import ProductCreateForm,RawDjangoProductForm

from .models import Product

# Create your views here.

def product_create_d_view(request,*args, **kwargs):
    #in case u wanna initialise ur regular Django form with some values:
    init_data_dict = {
       'title' : "My Django form title",
       'price' : 2000
    }
    my_form = RawDjangoProductForm(initial = init_data_dict)
    if request.method == "POST":
    	my_form = RawDjangoProductForm(request.POST,initial = init_data_dict)
    	if my_form.is_valid():#now the data is good    		
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
    	else:
    		print(my_form.errors)
    context = {"rawD_form": my_form}
    return render(request, "products/ProductCreate.html", context)

# def product_create_view(request,*args, **kwargs):
# 	if request.method == 'POST':
# 		ma_nu_title = request.POST.get('pop')
# 		print(ma_nu_title)
# 	context = {}
# 	return render(request, "products/ProductCreate.html", context)

def product_create_h_view(request,*args, **kwargs):
    #in case u wanna initialise ur Model form with some values:
    init_model_data_dict = {
       'title' : "My Model form title",
       'price' : 5000
    }
#   To edit existing model object:    
#   obj = Product.objects.get(id=1)
#   a_form = ProductCreateForm(request.POST or None, initial=init_data, instance=obj) 
    a_form = ProductCreateForm(request.POST or None, initial=init_model_data_dict)
    if a_form.is_valid():
    	a_form.save()
    	a_form = ProductCreateForm()
    context = {"html_form": a_form}
    return render(request, "products/ProductCreate.html", context)

# def dynamic_lookup(request,my_id,*args, **kwargs):
#     try:
#       my_obj = Products.object.get(id = my_id)
#     except Product.DoesNotExist:
#       raise Http404                   #to display Page not found using HTTP404
#     context = { "obj" : my_obj}
#     return render(request, "products/ProductDetail.html", context)

def dynamic_lookup(request,my_id,*args, **kwargs):
    my_obj = get_object_or_404(Product,id = my_id)  #to display Page nt found
    context = { "obj" : my_obj}
    return render(request, "products/ProductDetail.html", context)