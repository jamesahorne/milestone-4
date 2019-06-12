# from django.http import HttpResponse
from django.shortcuts import render
from products.models import Ticket
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Do I need this?
from django.contrib.auth.models import User

def index(request):
    ''' Index page '''
    return render(request, 'index.html')


def about(request):
    ''' About page '''
    return render(request, 'about.html')


def data(request):
    ''' Data page '''
    return render(request, 'data.html')


# def get_data(request):
#     # tickets = Ticket.objects.all()
#     tickets = serializers.serialize('json', Ticket.objects.all(), fields=('type', 'status', 'urgent'))

#     return HttpResponse(tickets)


class DataVisualisation(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        tickets = serializers.serialize('json', Ticket.objects.all(), fields=('type', 'status', 'urgent'))
        # usernames = [user.username for user in User.objects.all()]
        return Response(tickets)
