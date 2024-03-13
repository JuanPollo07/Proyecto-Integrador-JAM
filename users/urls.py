from django.urls import path
from users import views



urlpatterns = [
    path('register/', views.signUp.as_view(), name="register"),
    path('login/', views.logIn.as_view(), name="login"),
    path('logout/', views.logOut.as_view(), name="logout"),
    path('project/', views.project, name='create'),
]