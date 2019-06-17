from django.shortcuts import render
from products.models import Ticket
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    ''' Index page '''
    return render(request, 'index.html')


def about(request):
    ''' About page '''
    return render(request, 'about.html')


def data(request):
    ''' Data page '''
    return render(request, 'data.html')


class DataVisualisation(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        tickets = serializers.serialize('json', Ticket.objects.all(), fields=('type', 'status', 'urgent'))
        return Response(tickets)
