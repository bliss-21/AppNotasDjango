from django.urls import path
from .views import home, get_notes, post_note, delete_note, archived_note, get_note_by_id, update_note

urlpatterns = [   
    path('', home, name='home'),
    path('get_notes', get_notes, name='get_notes'),
    path('post_note', post_note, name='post_note'),
    path('delete_note/<id>', delete_note, name='delete_note'),
    path('archived_note/<id>', archived_note, name='archived_note'),
    path('get_note_by_id/<id>', get_note_by_id, name='get_note_by_id'),
    path('update_note/<id>', update_note, name='update_note'),
]