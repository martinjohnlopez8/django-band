from django import forms

from .models import Band, Album, Song, Member

class BandForm(forms.ModelForm):

	class Meta:
		model = Band
		fields = ('name', 'year_formed', 'place_of_origin', 'image_link', 'history')

class AlbumForm(forms.ModelForm):

	class Meta:
		model = Album
		fields = ('title', 'date_released', 'sales', 'band', 'image_link')

class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ('title', 'album', 'band')

class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ('name', 'band', 'image_link', 'instrument', 'biography')
