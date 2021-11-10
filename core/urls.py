from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('post1', views.post1, name= 'post1'),
    path('post2', views.post2, name= 'post2'),
    path('post3', views.post3, name= 'post3'),
]