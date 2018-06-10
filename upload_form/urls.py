from django.urls import path
from . import views

app_name = 'upload_form'

urlpatterns = [
    # ex: /
    path('', views.form, name='form'),

    # ex: /complete/
    # path('complete/', views.complete, name='complete'),

    path('download/', views.download, name='download'),
    # url(r'^download/(?P<p_id>\d+)/$', views.download, name='download'),  # 増えたのこれ
]
