from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip, Notes
from django.views.generic import CreateView,DetailView,ListView ,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Class-based view for home
class HomeView(TemplateView):
    template_name = 'trip/index.html'

# Function-based view to list trips
def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)  
    
    return render(request, 'trip/trips_list.html', {'trips': trips})

class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]  
    template_name = "trip/trip_form.html" 
    success_url = reverse_lazy("trip-list")  

    def form_valid(self, form):
        form.instance.owner = self.request.user 
        return super().form_valid(form)
    
class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    # template_name = "trip/trip_detail.html"
    # context_object_name = "trip"
    
    def get_context_data(self, **kwargs):
       
        context= super().get_context_data(**kwargs)
        trip=context['object']
        notes=trip.notes.all() 
        context['notes']=notes
        return context
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = "trip/notes_detail.html"  # Ensure this template exists
    context_object_name = "note"


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = "trip/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset= Notes.objects.filter(trip__owner=self.request.user)
        return queryset
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = "__all__"
    template_name = "trip/note_form.html"
    success_url = reverse_lazy("note-list")  

    def get_form(self):
        form=super(NoteCreateView,self).get_form()
        
        trips = Trip.objects.filter(owner=self.request.user)  
        form.fields['trip'].queryset=trips
        return form

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = "__all__"
    template_name = "trip/note_form.html"
    success_url = reverse_lazy("note-list")

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()

        # Filter trips so users can only select from their own trips
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips

        return form
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    # template_name = "trip/note_confirm_delete.html"
    success_url = reverse_lazy("note-list")



class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]  
    # template_name = "trip/trip_form.html"  
    success_url = reverse_lazy("trip-list")  

class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    # template_name = "trip/trip_confirm_delete.html"  
    success_url = reverse_lazy("trip-list")  

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)
