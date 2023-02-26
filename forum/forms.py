from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Entry, EntryType


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'entry_type', 'image', 'excerpt', 'content',)
        widgets = {
            'content': SummernoteWidget(),
        }
