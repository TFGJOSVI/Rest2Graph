from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('uploadFile', views.upload_file, name='uploadFile'),
    # path('apiContent', views.api_page, name='apiContent'),
]