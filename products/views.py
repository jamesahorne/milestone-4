from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Ticket
from .forms import TicketForm


def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'all_tickets.html', {"tickets": tickets})


@login_required
def buy_tickets(request):
    products = Product.objects.all()
    return render(request, 'buy_tickets.html', {"products": products})


@login_required
def bug(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            messages.success(request, "Your ticket was saved successfully.")
        else:
            messages.error(request, "There was an error, your ticket was not saved successfully.")
    else:
        ticket_form = TicketForm
    return render(request, 'bug.html', {"ticket_form": ticket_form})


@login_required
def feature(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            messages.success(request, "Your ticket was saved successfully.")
        else:
            messages.error(request, "There was an error, your ticket was not saved successfully.")
    else:
        ticket_form = TicketForm
    return render(request, 'feature.html', {"ticket_form": ticket_form})


def full_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views +=1
    ticket.save()
    return render(request, 'full_detail.html', {"ticket": ticket})
