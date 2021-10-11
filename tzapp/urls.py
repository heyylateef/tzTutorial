from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('settimezone', views.settimezone, name='settimezone')

]
