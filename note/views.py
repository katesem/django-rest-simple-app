from django.shortcuts import render, get_object_or_404
from .serializers import NotesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notes


@api_view(['GET', 'PUT', 'DELETE'])
def note_by_id_functionality(request, note_id):
    
    note = get_object_or_404(Notes, pk = note_id)
    
    if request.method == "GET": #gets note by id
        serializer = NotesSerializer(note)
        return Response(serializer.data)
    
        
    if request.method == "PUT": # updates note by id
        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE": # removes note by id 
        Notes.objects.get(pk = note_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    

@api_view(['GET', 'POST', 'DELETE'])
def all_notes_functionality(request):
    
    if request.method == "GET": # gets all notes from db
        all_notes = Notes.objects.all()
        serializer = NotesSerializer(all_notes, many=True)
        return Response(serializer.data)
        
    if request.method == "POST": # if successful - creates new note, else - continues without any changes
        post_data = {
            'name' : request.data.get('name'),
            'description' : request.data.get('description')
        }
        
        serializer  = NotesSerializer(data = post_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == "DELETE": #removes all notes from db
        deleted_notes = Notes.objects.all().delete()
        return Response()