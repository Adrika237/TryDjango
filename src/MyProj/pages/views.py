from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello World!</h1>")

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact page</h1>")

#def social_view(*args, **kwargs):
#	return HttpResponse("<h1>Social page</h1>")

def home2_view(request,*args, **kwargs):
	print(args,kwargs)
	print(request.user)
	return render(request, "home.html", {})

def contact2_view(request,*args, **kwargs):
	# print(args,kwargs)
	# print(request.user)
	my_context = { "my_txt":"ABCDEF", "my_num":100, "my_name" : "John", 
	"my_list" : [100,200, 'a', 'f']}
	return render(request, "Contact.html", my_context)

def social2_view(request,*args, **kwargs):
	print(args,kwargs)
	print(request.user)
	context_def = {"a_txt":"SOCIALTXT", "a_num":500, "a_name" : "Mia", 
	"yo_list" : [100,200, 'k', 'p', 'django', 300, 400]}
	return render(request, "Social.html", context_def)

def about2_view(request,*args, **kwargs):
	print(args,kwargs)
	print(request.user)
	my_context = { "my_txt":"SOMERANDOM", "my_num":100, 
	"my_name" : "Doe", "my_list" : [100,200, 'b', 'c']}
	return render(request, "About.html", my_context)