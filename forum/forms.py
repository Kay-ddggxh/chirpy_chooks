from django import forms
from .models import Entry, EntryType


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'entry_type', 'image', 'excerpt', 'content',)
