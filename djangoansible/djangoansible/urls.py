"""
URL configuration for djangoansible project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from ansibleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('', views.index),
    path('forward/', views.forward),
    path('backward/', views.backward),
    path('left/', views.left),
    path('right/', views.right),
    path('north/', views.north),
    path('south/', views.south),
    path('west/', views.west),
    path('east/', views.east),
    path('stop/', views.stop),
    path('stop2/', views.stop2),
    path('servomin/', views.servomin),
    path('servomid/', views.servomid),
    path('servomax/', views.servomax),
    path('servomin2/', views.servomin2),
    path('servomid2/', views.servomid2),
    path('servomax2/', views.servomax2),
    path('thirty/', views.thirty),
    path('fifty/', views.fifty),
    path('full/', views.full),
    path('eyeon/', views.eyeon),
    path('eyeoff/', views.eyeoff),
    path('fionaon/', views.fionaon),
    path('fionaoff/', views.fionaoff),
]
