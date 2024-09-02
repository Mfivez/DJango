from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render

def book_list(request):
    books = [
        {'title': 'DjangoDemo', 'author': 'fredou'},
        {'title': 'Python', 'author': 'yannick'}
    ]
    #return render(request, 'book_list.html', {'books': books})
    #return HttpResponse("Voici une réponse simple")
    #return JsonResponse({"nom":"django"})
