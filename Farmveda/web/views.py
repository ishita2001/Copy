from django.shortcuts import render, redirect
from web.forms import(
    BuyerRegistrationForm,
    SellerRegistrationForm,
    LoginForm,
    EditProfileForm
)
from django.http import HttpResponse
from django.contrib.auth import(
    login,
    logout,
    authenticate,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

loggedin = 'false'

def buyer_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('web:login_index')

    else:
        if request.method == 'POST':
            form = BuyerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('web:login_index')
        else:
            form = BuyerRegistrationForm()
        return render(request,'web/buyersignup.html',{'form':form})


def seller_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('web:login_index')

    else:
        if request.method == 'POST':
            form = SellerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('web:login_index')
        else:
            form = SellerRegistrationForm()
        return render(request,'web/sellersignup.html',{'form':form})        

def login_view(request):
        
        global loggedin

        if loggedin is 'true':
            return redirect('web:login_index')
    
        else:    
            if request.method == 'POST':
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    user = form.get_user()
                    loggedin = 'true'
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('web:login_index') 

            else:
                form = LoginForm()
            return render(request, 'web/login.html', {'form':form})

@login_required(login_url='/web/login/')
def my_profile(request):
    return render(request, 'web/myprofile.html',{'user':request.user})

@login_required(login_url='/web/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('web:my_profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'web/editprofile.html',{'form':form})
    


@login_required(login_url='/web/login/')
def login_index(request):
    return render(request, 'web/loggedin.html')

@login_required(login_url='/web/login/')
def logout_view(request):
    global loggedin
    if request.method == 'POST':
        loggedin = 'false'
        logout(request)
        return redirect('web:home')

def home(request):
    global loggedin

    if loggedin is 'true':
        return redirect('web:login_index')

    else:
        return render(request, 'web/homepage.html')

def signup_options(request):
    return render(request, 'web/options.html')

@login_required(login_url='/web/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('web:my_profile')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'web/changepassword.html',{'form':form})

def product(request,pk):
    user = request.user
    product = user.product_set.get(pk=pk)
    return render(request, 'web/productdetails.html',
        {   'user': request.user,
            'product':user.product_set.get(pk=pk),
        })


# Create your views here.
