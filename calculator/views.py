from django.shortcuts import render, redirect
from django.views import generic
from .forms import NewUserForm

from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

def calculator(request):
    calculatedvalue = 0
    expression = ""
    error_message = ""
    if request.method == "POST":  
        expression = request.POST['expression']
        try:
            calculatedvalue = eval(expression)
        except Exception as e:
            error_message = "Unable to evaluate your input !!"

    return render(request, 'calculator.html', {'calculatedvalue': calculatedvalue, 'expression': expression, 'error_message': error_message})


def userRegister(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("calculate")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="auth/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":

		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("calculate")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})
