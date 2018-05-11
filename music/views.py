from django.shortcuts import render, get_object_or_404
from .models import *



def index(request):
	all_playlist= Playlist.objects.all()
	
	context={'all_playlist':all_playlist }
	return render(request, 'music/index.html', context)

def details(request, playlist_id):
	playlist= get_object_or_404(Playlist, pk=playlist_id)
	return render(request, 'music/details.html', {'playlist':playlist})
	

def favorite(request, playlist_id):
	playlist= get_object_or_404(Playlist, pk=playlist_id)
	try:
		selected_song=playlist.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/details.html', {'playlist':playlist, 'error_message':'You did not select a valid song'})
	else:
		selected_song.is_favorite= True
		selected_song.save()
		return render(request, 'music/details.html', {'playlist': playlist})

		#playlist = Playlist.objects.get(pk=playlist_id)
		
	
	

# Create your views here.
