"""chat_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from chats.views import home,chats,aboutus,threadview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('chats/',chats,name='chats'),
    path('about-us/',aboutus,name='about-us'),
    path('accounts/',include('accounts.urls')),
    re_path(r"^chats/(?P<username>[\w.@+-]+)$",threadview,name='chatthread' ),

]
 