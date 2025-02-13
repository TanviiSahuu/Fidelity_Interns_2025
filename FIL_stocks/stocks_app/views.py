from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from stocks_app.models import stocks
from .forms import stockforms

# CREATE Operation
class add_stock(CreateView):
    model = stocks
    template_name = 'add.html'
    form_class = stockforms
    success_url = reverse_lazy('stock_list')  

# READ Operation
class show_stock(ListView):
    model = stocks
    template_name = 'stock_list.html'
    context_object_name = 'stocks'  

# UPDATE Operation
class update_stock(UpdateView):
    model = stocks
    template_name = 'update.html'
    fields='__all__'
    success_url = reverse_lazy('stock_list')
    # context_object_name = 'stocks'  


# DELETE Operation
class delete_stock(DeleteView):
    model = stocks
    template_name = 'delete_stock.html'  
    fields='__all__'
    success_url = reverse_lazy('stock_list')

# LOGIN Operation
def login_stock(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=uname).exists():
            messages.error(request, "Username doesn't exist. Please Sign Up.")
            return redirect('register_stock')

        user = authenticate(request, username=uname, password=password)

        if user is None:
            messages.error(request, "Invalid Password. Try Again.")
        else:
            login(request, user)
            messages.success(request, f"Welcome {uname}! You are now logged in.")
            return redirect('stock_list')

    return render(request, 'login.html')

# REGISTER Operation
def register_stock(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register_stock')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Choose another one.")
            return redirect('register_stock')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_stock')

    return render(request, 'register.html')

# LOGOUT Operation
def logout_stock(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('register_stock')