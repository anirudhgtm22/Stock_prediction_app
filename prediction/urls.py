from django.urls import path
from .views import LoginPageView,SignupApiView,LogoutView,SignupView,LoginAPIView,HomePageView
from .views import ProfileView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('loginpage/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/signup/', SignupApiView.as_view(), name='signup-api'),
    path('api/login/', LoginAPIView.as_view(), name='login-api'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]
