from django.urls import path

from . import views

app_name = 'band'
urlpatterns = [
    path('', views.band_list, name='band_list'),
    path('band/<int:band_id>', views.band_detail, name='band_detail'),
    path('band/<int:band_id>/edit/', views.edit_band, name='edit_band'),
    path('band/<int:band_id>/delete/', views.delete_band, name='delete_band'),
    path('band/<int:band_id>/album/<int:album_id>', views.album_detail, name='album_detail'),
    path('band/add/', views.add_band, name='add_band'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/add/', views.add_album, name='add_album'),
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/add/', views.add_song, name='add_song'),
    path('songs/<int:song_id>/edit/', views.edit_song, name='edit_song'),
    path('songs/<int:song_id>/delete/', views.delete_song, name='delete_song'),
    path('musicians/', views.musician_list, name='musician_list'),
    path('musicians/add/', views.add_musician, name='add_musician'),
    path('musicians/<int:musician_id>/edit/', views.edit_musician, name='edit_musician'),
    path('musicians/<int:musician_id>/delete/', views.delete_musician, name='delete_musician'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
