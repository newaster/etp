"""etp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('newetp', views.newetp, name='newetp'),
    path("",views.home, name="home"),
    path('admins/',views.admin,name="admin"),
    path('guest/',views.guest,name="guest"),
    path('user/',views.user,name="user"),
    path('signup/',views.signup_call,name="signup"),
    path('approval/',views.approval,name="approval"),
    path('logout/',views.logout_call,name="logout"),
    path('privacy/',views.privacy,name="privacy"),
    path('profile/',views.profile,name="profile"),
    path('hmi/',views.hmi,name="hmi"),
    path('faultreport/',views.faultreport,name="faultreport"),
    path('plantreport/',views.plantreport,name="plantreport"),
    path('createsite/',views.createsite,name="createsite"),
    path('managesite/',views.managesite,name="managesite"),
    path('editsite/<id>',views.editsite,name="editsite"),
    path('renewsite/<id>',views.renewsite,name="renewsite"),
    path('createuser/',views.createuser,name="createuser"),
    path('manageuser/',views.manageuser,name="manageuser"),
    path('edituser/<id>',views.edituser,name="edituser"),
    path('createzone/',views.createzone,name="createzone"),
    path('managezone/',views.managezone,name="managezone"),
    path('editzone/<id>',views.editzone,name="editzone"),
    path('createticket/',views.createticket,name="createticket"),
    path('manageticket/',views.manageticket,name="manageticket"),
    path('editticket/<id>',views.editticket,name="editticket"),
    path('hmi_view/',views.hmi_view)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

