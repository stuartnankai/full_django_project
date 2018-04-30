from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from users.forms import LoginForm


# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username)) # can use both email and username
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):

        login_form = LoginForm(request.POST) # check the form before going to the next step

        if login_form.is_valid():

            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html",
                              {"message": "Wrong username or password"})
        else:
            return render(request, "login.html", {"login_form":login_form})


# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#
#         user = authenticate(username=user_name, password=pass_word)
#
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"message": "Wrong username or password, please try again"})
#
#
#     elif request.method == "GET":
#         return render(request, "login.html", {})
