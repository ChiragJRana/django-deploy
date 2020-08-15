from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InstrumentsSerializer
from .models import Instruments
# Create your views here.

# class instrumentList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Instruments.objects.all()
#         serializer = InstrumentsSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = InstrumentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def apiOverview(request):
    
    api_urls = {
        'List':'/instrument-list/',
        'Detail': '/instrument-detail/<str:pk>',
        'Create': '/instrument-create/',
        'Updtae':'/instrument-update/<str:pk>',
        'Delete': '/instrument-delete/<str:pk>',
        }

    return Response(api_urls)

@api_view(['GET'])
def instrumentList(request):
    instruments = Instruments.objects.all()
    serializer = InstrumentsSerializer(instruments, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def instrumentDetail(request,pk):
    instrument = Instruments.objects.get(id = pk)
    serializer = InstrumentsSerializer(instrument, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def instrumentCreate(request):
    serializer = InstrumentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['POST'])
def instrumentUpdate(request, pk):
    task = Instrument.objects.get(id=pk)
    serializer = InstrumentsSerializer(instance = task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def instrumentDelete(request, pk):
    task = Instrument.objects.get(id=pk)
    task.delete()

    return Response('Item Succeesfully deleted!')