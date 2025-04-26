

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('book_list/', views.book_list, name='book_list'),  # Danh sách sách
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # Chi tiết sách
]
