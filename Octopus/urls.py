"""Octopus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Apps.Web.views import home,result,sign_in,sign_up,sign_in_data,sign_out,account,sign_up_data,account_edit,account_edit_data
#from Apps.AI_Bucket.views import call_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('result',result,name='result'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('sign_in_data', sign_in_data, name='sign_in_data'),
    path('sign_out', sign_out, name='sign_out'),
    path('account', account, name='account'),
    path('sign_up_data',sign_up_data,name='sign_up_data'),
    path('account_edit',account_edit,name='account_edit'),
    path('account_edit_data',account_edit_data,name='account'),

]
#    path('model/',call_model.as_view())