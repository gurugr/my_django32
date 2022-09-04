from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login


def user_registration(request):
    print("i'm going to register now")
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("I'm registered now")
        return redirect("/login")
    context = {"form":form}
    return render(request,"accounts/user_registration.html",context)

# Create your views here.
def loging_view(request):
    if request.method == 'POST':
        print("loggin")
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            login(request,user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)

    context = {"form":form}
    return render(request,"accounts/login_view.html",context=context)

def log_out_view(request):
    logout(request)
    print("i'm log out")
    return redirect("/login/")
    # return render(request,"accounts/login_view.html")

