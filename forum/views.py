from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def entry_detail(request, slug):
    """
    Displays individual forum entry
    """

    entry = get_object_or_404(Entry, slug=slug)

    context = {
        'entry': entry,
    }

    return render(request, 'forum/entry_detail.html', context)


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
            # return redirect(reverse('entry_detail', args=[entry.slug]))
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


@login_required
def edit_entry(request, slug):
    """ Edit a forum post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    entry = get_object_or_404(Entry, slug=slug)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited forum post!')
            return redirect(reverse('entry_detail', args=[entry.slug]))
        else:
            messages.error(
                request,
                'Failed to update post. Please ensure the form is valid.')
    else:
        form = EntryForm(instance=entry)
        messages.info(
            request,
            f'You are editing the forum post "{entry.title}"')

    template = 'forum/edit_entry.html'
    context = {
        'form': form,
        'entry': entry,
    }

    return render(request, template, context)


@login_required
def delete_entry(request, slug):
    """ Delete forum entry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    entry = get_object_or_404(Entry, slug=slug)
    entry.delete()
    messages.success(request, 'Forum post was deleted.')
    return redirect('/forum/')
