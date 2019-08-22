from django.shortcuts import render
from products.models import Ticket


def search(request):
    ''' Search for a ticket by its name '''
    tickets = Ticket.objects.filter(issue_name__icontains=request.GET['searchbox'])
    return render(request, 'all_tickets.html', {"tickets": tickets})
