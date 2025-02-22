"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,trips_list,TripDeleteView,TripUpdateView,TripCreateView,TripDetailView,NoteDetailView,NoteListView,NoteCreateView,NoteUpdateView,NoteDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trip-list'),
    path('dashboard/note/', NoteListView.as_view(), name='note-list'),
    path('dashboard/note/create', NoteCreateView.as_view(), name='note-create'),
    path("dashboard/trip-create", TripCreateView.as_view(), name="trip-create"),
    path("dashboard/trip/<int:pk>", TripDetailView.as_view(), name="trip-detail"),
    
    path("dashboard/trip/<int:pk>/edit/", TripUpdateView.as_view(), name="trip-update"),
    path("dashboard/trip/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"),

    
    path("dashboard/note/<int:pk>", NoteDetailView.as_view(), name="note-detail"),
    
    path("dashboard/note/<int:pk>/edit/", NoteUpdateView.as_view(), name="note-update"),
    path("dashboard/note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
    
]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
