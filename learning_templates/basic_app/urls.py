from django.urls import path,re_path, include
from basic_app import views



# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$', views.relative, name = 'relative' ),
    re_path(r'^other/$', views.other, name = 'other'),

]
