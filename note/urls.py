from django.urls import path, include
from . import views


urlpatterns = [
    path('/<int:note_id>', views.note_by_id_functionality, name = 'note_functionality'),
    path('', views.all_notes_functionality, name = 'all_notes_functionality')
]