from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializer import BookSerializer


# Create your views here.

class BookList(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class CreateBooks(APIView):
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class book(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except:
            return Response(
                {'error':'the resouce aint available at the momment'}, 
                status=status.HTTP_404_NOT_FOUND
            )


    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data= request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': 'the content cant be update'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

