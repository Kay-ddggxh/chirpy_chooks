from django.contrib import admin
from .models import Entry, EntryType


@admin.register(EntryType)
class EntryTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'entry_type',
        'create_date',
    )
