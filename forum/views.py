from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Entry, EntryType
from .forms import EntryForm


def entry_list(request):
    """
    Renders all forum entries
    """
    entries = Entry.objects.all()

    context = {
        'entries': entries,
    }

    return render(request, 'forum/forum.html', context)


@login_required
def create_entry(request):
    """ Create forum post """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can write forum posts.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            messages.success(request, 'New entry was posted to forum!')
            # return redirect(reverse('product_detail', args=[product.id]))
            return redirect(reverse('forum'))
        else:
            messages.error(
                request,
                'Could not post new entry. Please ensure the form is valid.')
    else:
        form = EntryForm()

    template = 'forum/create_entry.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
