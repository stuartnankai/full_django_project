from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from users.forms import LoginForm, RegisterForm, ForgetForm,ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email


# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # can use both email and username
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html",
                              {"register_form": register_form, "message": "This email had been used"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            # user_profile.is_active = True
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):

        login_form = LoginForm(request.POST)  # check the form before going to the next step

        if login_form.is_valid():

            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html",
                                  {"message": "The user is not active"})
            else:
                return render(request, "login.html",
                              {"message": "Wrong username or password"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class ForgetPwd(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            send_register_email(email,"forget")
            return render(request,'send_success.html')
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, reset_code):
        print("This is reset code : ", reset_code)
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html',{"email":email})
class ModifyPwdView(View):
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1","")
            pwd2 = request.POST.get("password2","")
            email = request.POST.get("email")
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email,"message":"Not the same password"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get("email")
            return render(request, 'password_reset.html', {"email": email, "modify_form": modify_form})
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
