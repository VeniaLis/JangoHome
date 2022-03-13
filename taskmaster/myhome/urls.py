from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
]