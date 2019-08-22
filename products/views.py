from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Ticket
from .forms import TicketForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def all_tickets(request):
    ''' Displays all tickets. Can be filtered by name with the search box '''
    tickets = Ticket.objects.all().order_by('-published_date')
    return render(request, 'all_tickets.html', {"tickets": tickets})


@login_required
def buy_tickets(request):
    ''' Buy bugs, features or upvotes '''
    products = Product.objects.all()
    return render(request, 'buy_tickets.html', {"products": products})


@login_required
def bug(request):
    ''' Fill out form to post a bug '''
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.type = 'Bug'
            ticket.save()
            messages.success(request, "Your ticket was saved successfully.")
            return redirect(reverse('all_tickets'))
        else:
            messages.error(request, "There was an error, your ticket was not saved successfully.")
    else:
        ticket_form = TicketForm
    return render(request, 'bug.html', {"ticket_form": ticket_form})


@login_required
def edit_ticket(request, pk):
    ''' Fill out form to edit a ticket '''
    ticket = get_object_or_404(Ticket, pk=pk)
    if (request.user.is_authenticated and request.user == ticket.author or
            request.user.is_superuser):
        if request.method == "POST":
            ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
            if ticket_form.is_valid():
                ticket_form.save()
                messages.success(request, "Your ticket was saved successfully.")
                return redirect(full_detail, ticket.pk)
            else:
                messages.error(request, "There was an error, your ticket was not saved successfully.")
        else:
            ticket_form = TicketForm(instance=ticket)
    else:
        return HttpResponseForbidden()
    return render(request, 'edit_ticket.html', {'ticket_form': ticket_form})


@login_required
def feature(request):
    ''' Fill out form to post a feature '''
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.type = 'Feature'
            ticket.save()
            messages.success(request, "Your ticket was saved successfully.")
            return redirect(reverse('all_tickets'))
        else:
            messages.error(request, "There was an error, your ticket was not saved successfully.")
    else:
        ticket_form = TicketForm
    return render(request, 'feature.html', {"ticket_form": ticket_form})


def full_detail(request, pk):
    ''' Displays full details of a specific ticket '''
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views +=1
    ticket.save()
    return render(request, 'full_details.html', {"ticket": ticket})


@login_required
def feature_or_upvote(request):
    ''' Choose to upvote a feature or post a feature '''
    return render(request, "feature_or_upvote.html")


@login_required
def upvote(request):
    ''' Upvote a feature that is still to be added '''
    tickets = Ticket.objects.filter(type="Feature", status="ToDo")
    return render(request, "upvote.html", {"tickets": tickets})


def add_upvote(request, pk):
    ''' Upvote a bug or feature '''
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes +=1
    ticket.save()
    return redirect(reverse('full_detail', args=[pk]))
