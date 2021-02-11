from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import UserSignUp
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages 
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

# Create your views here.
#Views for SignUp form
def u_signup(request):
    form = UserSignUp()
    if request.method=='POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            #F_name = form.cleaned_data['first_name']
            #messages.success(request,f'Congrats {F_name}, You can Login Now!')
            form.save()
            return redirect('login')
    return render(request,'core/signup.html',{'form':form})

#Views for Login Form
def u_login(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            user = authenticate(username=u_name,password=u_pass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
    return render(request,'core/login.html',{'form':form})

#Views for Change password
def u_change(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                #messages.success(request,'Password Changed Successfully')
                form.save()
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'core/changepass.html',{'form':form})
    else:
        
        return HttpResponseRedirect('/login/')


#views for Dashboard
def u_dashboard(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        return render(request,'core/dashboard.html',{'name':name})
    else:
        return HttpResponseRedirect('/login/')

#views for Logout

def u_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')