"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from myblog.views import Home_View
from myblog.views import DetailArticleView
from myblog.views import AddPostView
from members.views import UserRegisterView
from myblog.views import search_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home_View.as_view(), name='home'),
    path('article/<int:pk>',DetailArticleView.as_view(),name='article-detail'),
    path('addpost/',AddPostView.as_view(),name='add_post'),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',UserRegisterView.as_view(),name='register'),
    path('searchuser/',search_user,name='searchuser')

]+ static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
