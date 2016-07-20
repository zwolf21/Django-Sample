from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# Create your views here.

class BooksModelView(TemplateView):
	template_name = 'books/index.html'

	def get_context_data(self, **kwargs):
		context = super(BooksModelView, self).get_context_data(**kwargs)
		context['object_list'] = ['Book', 'Author', 'Publisher']
		return context

class BookList(ListView):
	def __init__(self):
		super(BookList, self).__init__()
		print('a')

	model = Book

class AuthorList(ListView):
	model = Author

class PublisherList(ListView):
	model = Publisher


class BookDetail(DetailView):
	model = Book

class AuthorDetail(DetailView):
	model = Author

class PublisherDetail(DetailView):
	model = Publisher

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		