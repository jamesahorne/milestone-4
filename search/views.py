from django.shortcuts import render
from products.models import Ticket


def search(request):
    tickets = Ticket.objects.filter(issue_name__icontains=request.GET['q'])
    return render(request, 'all_tickets.html', {"tickets": tickets})
