"""myback1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('logout/', views.logout, name = 'logout'),
    path('index/', views.index),
    #问题信息
    path('questionlist/', views.questionlist),
    path('questionadd/', views.questionadd),
    path('questionedit/<int:id>/', views.questionedit),
    path('questiondel/<int:id>/', views.questiondel),

    #用户信息
    path('userlist/', views.userlist),
    path('useredit/<int:id>/',views.useredit),
    path('useradd/', views.useradd),
    path('userdel/<int:id>/', views.userdel),

    #做题记录
    path('recordlist/',views.recordlist),
    path('recordadd/',views.recordadd),
    path('recorddel/<int:id>/', views.recorddel),
    path('recordedit/<int:id>/',views.recordedit),
]
