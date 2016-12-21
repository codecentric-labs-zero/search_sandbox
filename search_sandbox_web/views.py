from django.shortcuts import render
from django.http import HttpResponse
from search_sandbox_web.models import Note
import os

import random
import json


def add_random_note(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'MOCK_DATA.json')
    line = open(file_path).read().replace("'", '"')  # Format JSON
    projNames = json.loads(line)  # Load list
    random_data = random.choice(projNames)

    new_note = Note()
    new_note.title = random_data['title']
    new_note.body = random_data['body']
    new_note.pub_date = random_data['pub_date']
    new_note.save()

    return render(request, 'note_added.html', {'note': random_data})


def notes(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})
