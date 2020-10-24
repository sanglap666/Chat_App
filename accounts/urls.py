from django.urls import path
from chats import views as chat_views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',chat_views.home),
    path('log-in/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('log-out/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('sign-in/',accounts_views.signin,name='signin'),
]
