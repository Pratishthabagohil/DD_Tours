from django.contrib import admin
from .models import Location, Contact, Itinerary, Inquiry

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'difficulty', 'price')
    search_fields = ('name', 'difficulty')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')

