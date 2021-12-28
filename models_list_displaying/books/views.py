from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)

def book_view(request, date):
    template = 'books/books_list.html'
    all_dates = [i[0].strftime('%Y-%m-%d') for i in Book.objects.order_by('pub_date').distinct().values_list('pub_date')]
    books_on_date = Book.objects.filter(pub_date=date)
    if date in all_dates:
        date_index = all_dates.index(date)
        page = date_index + 1
        paginator = Paginator(all_dates, 1)
        p = paginator.get_page(page)
        context = {
            'books': books_on_date,
            'page': p,
            'previous_date': '',
            'next_date': ''
        }
        if 1 <= date_index < len(all_dates) - 1:
            context['previous_date'] = all_dates[date_index -1]
            context['next_date'] = all_dates[date_index + 1]
        elif date_index == 0:
            context['next_date'] = all_dates[date_index + 1]
        elif date_index == len(all_dates) - 1:
            context['previous_date'] = all_dates[date_index - 1]
    else:
        context = {}
    return render(request, template, context)
