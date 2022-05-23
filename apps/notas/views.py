from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

#move to util.py
def nota_serializer(nota):

    json = {
        'id':nota.id,
        'title': nota.title, 
        'description': nota.description, 
        'create': str(nota.create), 
        'archived': nota.archived, 
        'deleted': nota.deleted, 
        'deleted_datetime': str(nota.deleted_datetime), 
    }

    return json

# Create your views here.
def home(request):
    
    return render(request,'notas/home.html')

def get_notes(request):
    notes = Note.objects.filter(deleted = False, archived = False)
    cant_notes = notes.count()
    notes = [nota_serializer(note) for note in notes]

    data = {
        'OK':True,
        'cant':cant_notes,
        'data':notes,
    }

    return HttpResponse(json.dumps(data), content_type='application/json')

def get_note_by_id(request, id):

    try:

        note = Note.objects.get(deleted = False, archived = False, id=id)

        note = nota_serializer(note)

        data = {
            'OK':True,
            'data':note,
        }
    except:
        data = {
            'OK':False,
            'Message':'No se pudo Obtener la Nora',
        }

    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def post_note(request):
    
    data = {}
    
    try:
        json_nota = request.body.decode()
        json_nota = json.loads(json_nota)
        note = Note()

        note.title = json_nota["title"]
        note.description = json_nota["description"]
        note.save()

    except:

        data['OK'] = False
        data['Message'] = 'No se a Creado la Nota'

        return HttpResponse(json.dumps(data), content_type='application/json')

    data['OK'] = True

    return HttpResponse(json.dumps(data), content_type='application/json')

def delete_note(request, id):

    data = {}
        
    try:
        
        note = Note.objects.get(id = id)
        note.deleted = True
        note.deleted_datetime = datetime.datetime.now() 
        note.save()

    except:

        data['OK'] = False
        data['Message'] = 'No se elimino la Nota'

        return HttpResponse(json.dumps(data), content_type='application/json')

    data['OK'] = True

    return HttpResponse(json.dumps(data), content_type='application/json')

def archived_note(request, id):

    data = {}
        
    try:
        
        note = Note.objects.get(id = id)
        note.archived = True
        note.save()

    except:

        data['OK'] = False
        data['Message'] = 'No se archivo la Nota'

        return HttpResponse(json.dumps(data), content_type='application/json')

    data['OK'] = True

    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def update_note(request, id):
    
    data = {}
    
    try:
        json_nota = request.body.decode()
        json_nota = json.loads(json_nota)

        note = Note.objects.get(deleted = False, archived = False, id=id)
        note.title = json_nota["title"]
        note.description = json_nota["description"]
        note.save()

    except:

        data['OK'] = False
        data['Message'] = 'No se a Actializado la Nota'

        return HttpResponse(json.dumps(data), content_type='application/json')

    data['OK'] = True

    return HttpResponse(json.dumps(data), content_type='application/json')
