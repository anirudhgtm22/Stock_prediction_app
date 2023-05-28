from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as django_login



class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user) 
            return Response({'message': 'Login successful','authentication': True}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials','authentication': False}, status=status.HTTP_401_UNAUTHORIZED)





class SignupApiView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            print("coming here")
            serializer.save()
            print("hello")
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomePageView(TemplateView):
    template_name = 'home.html'

class LoginPageView(LoginView):
    template_name = 'loginpage.html'
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return self.form_invalid(form)

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'signup.html', {'form': form})

class LogoutView(RedirectView):
    url = reverse_lazy('home')  

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
    
class ProfileView(TemplateView):
    template_name = 'profile.html'


