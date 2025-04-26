from django.shortcuts import render, get_object_or_404
from .models import Book
from django.core.paginator import Paginator

def home(request):
    # Lấy 5 cuốn sách nổi bật
    featured_books = Book.objects.all()[:5]  # Lấy 5 sách đầu tiên
    return render(request, 'MyApp/home.html', {'featured_books': featured_books})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 9)  # Hiển thị 9 sách mỗi trang
    page_number = request.GET.get('page')  # Lấy số trang từ URL
    page_obj = paginator.get_page(page_number)  # Lấy đối tượng page

    return render(request, 'MyApp/book_list.html', {'page_obj': page_obj})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'MyApp/book_detail.html', {'book': book})
