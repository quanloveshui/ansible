from django.conf.urls import url
from myansible import views

app_name = 'ansible'

urlpatterns = [
    url(r'^$', views.ansible_index),
    url(r'^result/', views.ansible_api),
    url(r'^listhost/', views.display)
]
