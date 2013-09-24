from django.http import HttpResponse
from books.models import Book
from django.shortcuts import render
import csv
# Create your views here.

def search_form(request):
    return render(request,'search_form.html')


def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		return render(request,'search_results.html',{'books':books,'query':q,})		
	else:
		return render(request, 'search_form.html', {'error': True})
		#return HttpResponse('Please submit a search form')

#def  search(request):
#	if 'q' in request.GET:
#		q = request.GET['q']
#		if not q:
#			error = True
#		else
#		books = Book.objects.filter(title__icontains=q)
#		return render(request, 'search_results.html',{'books': books, 'query': q})
#		return render(request, 'search_form.html', {'error': True})

def search_test(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

def my_image(request):
	image_data = open("/home/vinothini/Pictures/images.jpg","rb").read()
	return HttpResponse(image_data,mimetype="image/jpg")


