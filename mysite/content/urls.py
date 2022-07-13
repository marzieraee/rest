from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.PostListApi.as_view(), name='postlistapi'),
    path('apidetail/<int:pk>', views.PostDetailApi.as_view(), name='postlistapi'),
    
]