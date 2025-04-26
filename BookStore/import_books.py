import os
import django
import csv

# Khởi động Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookStore.settings')
django.setup()

from MyApp.models import Book  # đúng tên app/models nhé

with open(r'C:\Users\admin\pythonweb\github\Bookstore\Django-BookStore\Book_Dataset_1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Book.objects.create(
            title=row.get('Title', 'No Title'),
            genre=row.get('Category', 'Unknown'),
            price=float(row.get('Price', 0)),
            description=row.get('Book_Description', ''),
            image=row.get('Image_Link', ''),
            rating=float(row.get('Stars', 0))
        )
print("Import thành công!")
