from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


def login(request):
    pass

# 새로운 user 인스턴스를 만드는 것
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form=UserCreationForm()

    return render(request,"accounts/signup_form.html",{
        "form":form,
    })

# signup=CreateView.as_view(
#     form_class=UserCreationForm,
#     success_url=reverse_lazy("accounts:login"),
#     template_name="accounts/signup_form.html",
# )

def profile(request):
    pass

def logout(request):
    pass