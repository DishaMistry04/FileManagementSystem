from django.shortcuts import render,redirect
from rest_framework.response import Response
from . models import *
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
from rest_framework.generics import *
from .serializer import SignupSerializer,LoginSerializer
from rest_framework.views import APIView

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/filenest')

    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            u = f.save(commit=False)
            u.username = u.email
            u.set_password(u.password)
            u.save()
            return redirect('/login')
        else:
            d = {'form': f, 'message': 'Passwords do not match.'}
            return render(request, 'signup.html', d)

    else:
        f = UserForm()
        d = {'form': f}
        return render(request, "signup.html", d)

def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            try:
                u = Users.objects.get(email=email)
                user = authenticate(
                    request,
                    username=u.username,
                    password=password
                )

                if user is not None:
                    auth_login(request, user)
                    return redirect('/filenest')
                else:
                    messages.error(request, "Incorrect Password")

            except Users.DoesNotExist:
                messages.error(request, "Email does not exist")
    else:
        f = LoginForm()
    d = {'form': f}
    return render(request, "login.html", d)

def logout_user(request):
    logout(request)
    return redirect('/')

class CreateUser(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = SignupSerializer


class LoginUser(APIView):
    def post(self, request):
        f = LoginSerializer(data=request.data)
        if f.is_valid():
            email = f.validated_data['email']
            password = f.validated_data['password']
            try:
                u = Users.objects.get(email=email)
                user = authenticate(
                    request,
                    username=u.username,
                    password=password
                )

                if user is not None:
                    auth_login(request, user)
                    return Response({"message": "Login Successful"})
                else:
                    return Response({"message": "Incorrect Password"})
            except Users.DoesNotExist:
                return Response({"message": "Email does not exist"})

