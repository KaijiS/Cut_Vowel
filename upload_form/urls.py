from django.urls import path
from . import views

app_name = 'upload_form'

urlpatterns = [
    path('', views.form, name='form'),
    path('download/', views.download, name='download'),
]
