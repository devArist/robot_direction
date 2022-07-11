from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'message': 'Bienvenue sur notre API'})

@api_view(['GET'])
def devant(request):
    return Response({'message': 'OK'})

@api_view(['GET'])
def arriere(request):
    return Response({'message': 'OK'})

@api_view(['GET'])
def gauche(request):
    return Response({'message': 'OK'})

@api_view(['GET'])
def droite(request):
    return Response({'message': 'OK'})

@api_view(['GET'])
def stop(request):
    return Response({'message': 'OK'})