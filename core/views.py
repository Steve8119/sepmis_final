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



from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Unit, Notification, ChatMessage

@login_required
def u_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)  # Fetch the profile related to the user
        units = profile.units.all()  # Fetch all units related to the profile
        notifications = profile.notifications.all()  # Fetch all notifications related to the profile
        chat_messages = ChatMessage.objects.filter(receiver=user)  # Fetch chat messages for the user

        context = {
            'name': user.get_full_name(),
            'username': user.username,
            'email': user.email,
            'full_name': profile.full_name,  # Add full_name to the context
            'admission_number': profile.admission_number,
            'course': profile.course,
            'year_of_studies': profile.year_of_studies,
            'units': units,  # Add units to the context
            'total_fees': profile.total_fees,
            'fees_balance': profile.fees_balance,
            'notifications': notifications,
            'chat_messages': chat_messages,
        }
        return render(request, 'core/dashboard.html', context)
    else:
        return HttpResponseRedirect('/login/')


def u_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')
    













# views.py

# from django.shortcuts import render, redirect
# from .models import Profile
# from django.contrib import messages

# def save_units(request):
#     if request.method == 'POST':
#         unit_names = request.POST.getlist('unit_name[]')

#         # Assuming you have access to the user's profile
#         user_profile = request.user.profile

#         # Save units in the database
#         for unit_name in unit_names:
#             StudentUnits.objects.create(
#                 user_profile=user_profile,
#                 unit_name=unit_name,
#             )

#         messages.success(request, 'Units saved successfully.')
#         return redirect('dashboard')  # Redirect to dashboard or any other page
#     return render(request, 'dashboard.html')






from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def save_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.save()
        return redirect('dashboard')  # Redirect to the dashboard or any other page after saving

    return redirect('dashboard')
