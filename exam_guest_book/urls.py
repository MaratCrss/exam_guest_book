"""exam_guest_book URL Configuration

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
from django.urls import path

from webapp.views import index_view, create_record, delete_record, update_record, search_record

urlpatterns = [
    path('', index_view, name='index'),
    path('create_record/', create_record, name='create_record'),
    path('delete_record/<int:pk>/', delete_record, name='delete_record'),
    path('update_record/<int:pk>/', update_record, name='update_record'),
    path('search_record/', search_record, name='search_record'),
]