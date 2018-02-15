from django.shortcuts import render
from .forms import BandForm, AlbumForm, SongForm, MemberForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as band_logout
from django.contrib.auth import login as band_login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Band, Album, Song, Member

# Create your views here.

def band_list(request):
	if request.POST.get('search-band'):
		bands = Band.objects.filter(name__icontains=request.POST.get('band-input')).order_by('name')
		return render(request, 'band/index.html', {'bands': bands})
	else:
		bands = Band.objects.all().order_by('name')
		return render(request, 'band/index.html', {
			'bands': bands,
	})

def album_list(request):
	if request.POST.get('search-album'):
		albums = Album.objects.filter(title__icontains=request.POST.get('album-input')).order_by('title')
		return render(request, 'band/album_list.html', {'albums': albums})
	albums = Album.objects.all().order_by('title')
	return render(request, 'band/album_list.html', {
		'albums': albums
	})

def song_list(request):
	if request.POST.get('search-song'):
		songs = Song.objects.filter(title__icontains=request.POST.get('song-input')).order_by('title')
		return render(request, 'band/song_list.html', {'songs': songs})
	songs = Song.objects.all().order_by('title')
	return render(request, 'band/song_list.html', {
		'songs': songs
	})

def musician_list(request):
	if request.POST.get('search-musician'):
		members = Member.objects.filter(name__icontains=request.POST.get('musician-input')).order_by('name')
		return render(request, 'band/musician_list.html', {'members': members})
	members = Member.objects.all().order_by('name')
	return render(request, 'band/musician_list.html', {
		'members': members
	})

def band_detail(request, band_id):
	band = Band.objects.get(id=band_id)
	albums = Album.objects.filter(band__pk=band_id)
	members = Member.objects.filter(band__pk=band_id)
	return render(request, 'band/band_detail.html', {
		'band': band,
		'albums': albums,
		'members': members
	})

def album_detail(request, band_id, album_id):
	songs = Song.objects.filter(album__pk=album_id)
	return render(request, 'band/album_detail.html', {
		'songs': songs
	})

@login_required
def add_band(request):
	if request.method == 'POST':
		form = BandForm(request.POST)
		if form.is_valid():
			band = form.save(commit=False)
			band.save()
			return redirect('band:band_list')
	else:
		form = BandForm()
	return render(request, 'band/add_band.html', {
		'form': form
	})

@login_required
def add_album(request):
	if request.method == 'POST':
		form = AlbumForm(request.POST)
		if form.is_valid():
			album = form.save(commit=False)
			album.save()
			return redirect('band:album_list')
	else:
		form = AlbumForm()
	return render(request, 'band/add_album.html', {
		'form': form
	})

@login_required
def edit_album(request, album_id):
	album = Album.objects.get(id=album_id)
	if request.method == "POST":
		form = AlbumForm(request.POST, instance=album)
		if form.is_valid():
			album.save()
			return redirect('band:album_list')
	else: 
		form = AlbumForm(instance=album)
	return render(request, 'band/edit_album.html', {
		'form': form,
	})

@login_required
def add_song(request):
	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			song = form.save(commit=False)
			song.save()
			return redirect('band:song_list')
	else:
		form = SongForm()
	return render(request, 'band/add_song.html', {
		'form': form
	})

@login_required
def add_musician(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			member = form.save(commit=False)
			member.save()
			return redirect('band:musician_list')
	else:
		form = MemberForm()
	return render(request, 'band/add_musician.html', {
		'form': form
	})

@login_required
def edit_band(request, band_id):
	band = Band.objects.get(id=band_id)
	if request.method == "POST":
		form = BandForm(request.POST, instance=band)
		if form.is_valid():
			# band = band.save(commit=False)
			band.save()
			return redirect('band:band_detail', band_id)
	else:
		form = BandForm(instance=band)
	return render(request, 'band/edit_band.html', {
		'form': form,
	})

@login_required
def delete_album(request, album_id):
	album = Album.objects.get(id=album_id)
	album.delete()
	return redirect('band:album_list')

@login_required
def delete_band(request, band_id):
	band = Band.objects.get(id=band_id)
	band.delete()
	return redirect('band:band_list')

@login_required
def edit_song(request, song_id):
	song = Song.objects.get(id=song_id)
	if request.method == "POST":
		form = SongForm(request.POST, instance=song)
		if form.is_valid():
			song.save()
			return redirect('band:song_list')
	else: 
		form = SongForm(instance=song)
	return render(request, 'band/edit_song.html', {
		'form': form,
	})

@login_required
def delete_song(request, song_id):
	song = Song.objects.get(id=song_id)
	song.delete()
	return redirect('band:song_list')

@login_required
def edit_musician(request, musician_id):
	member = Member.objects.get(id=musician_id)
	if request.method == "POST":
		form = MemberForm(request.POST, instance=member)
		if form.is_valid():
			member.save()
			return redirect('band:musician_list')
	else:
		form = MemberForm(instance=member)
	return render(request, 'band/edit_musician.html', {
		'form': form
	})

@login_required
def delete_musician(request, musician_id):
	member = Member.objects.get(id=musician_id)
	member.delete()
	return redirect('band:musician_list')

def login(request):
	if request.POST.get('login'):
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        band_login(request, user)
	        return redirect('band:band_list')
	    else:
	        print('Error logging in')
	elif request.POST.get('signup'):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			band_login(request, user)
			return redirect('band:band_list')
	form = UserCreationForm()
	return render(request, 'band/login.html', {
		'form': form
	})

def logout(request):
	band_logout(request)
	return redirect('band:band_list')