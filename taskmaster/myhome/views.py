from django.http import HttpResponse
from django.shortcuts import render

from .models import Book,Review


def home(request):
    return render(request, 'home.html')

def book_detail(request, book_id):
    # return HttpResponse(f'Your book id is {book_id}')
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})