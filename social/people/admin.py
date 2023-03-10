from django.contrib import admin

from .models import *



class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


 admin.site.registrer(People, PeopleAdmin)