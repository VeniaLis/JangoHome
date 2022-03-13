from django.contrib import admin
from django.urls import path

from myhome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]
